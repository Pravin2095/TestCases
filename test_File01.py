from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_argument("headless")
Service_Object = Service()

import pytest

class Test_Cases:                          # Class name must be in Capital latter otherwise it's showed 'Empty Suite'.

    @pytest.mark.Arithmatic
    def test_Addition(self):
        A = 5
        B = 10
        Addition = A + B
        print(Addition)

        if Addition == 15:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Minus(self):
        C = 236
        D = 126
        Minus = C - D
        print(Minus)

        if Minus == 110:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Multi(self):
        A = 5
        B = 15
        Multi = A * B
        print(Multi)

        if Multi == 75:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")



    def Multi(self):                         # This test case not displyed because of prefix name 'test_'.
        A = 5
        B = 15
        Multi = A * B
        print(Multi)

        if Multi == 75:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Division(self):
        A = 150
        B = 3
        Division = A // B
        print(Division)

        if Division == 50:
            assert True         # assert is check condition according to the code otherwise it's give 'Assertion Error'.
        else:
            assert False

    def test_YouTube(self):

        Driver = webdriver.Chrome(options = Chrome_Options)
        Driver.get("https://www.youtube.com/")

        Driver.implicitly_wait(10)

        Logo = Driver.find_element(By.XPATH,"//ytd-topbar-logo-renderer[@id='logo']").is_displayed()
        print(Logo)

        if Logo == True:
            assert True          # Condition has satisfied then it status is --> PASSED
        else:
            assert False         # Conditions has not satisfied then it status is --> FAILED


    def test_Google(self):

        Driver = webdriver.Chrome(options = Chrome_Options)
        Driver.get("https://www.google.co.in/")

        Image = Driver.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        print(Image)

        if Image == True:
            assert True
        else:
            assert False


# Program or test case run in terminal also :
#                                              Use : pytest    (For run program and testcase)
#                                    More Detailed : pytest -v (For more detailed way to run program and testcase)

# In terminal to run the Files to use as pytest or pytest -v:
#                                                            It runs all files which are open on window.

# For specific file or testcase to run in terminal which are open on window:
#                                                               For File   : pytest File_Name
#                                                             For testCase : pytest File_Name>TestCase_Name
# To clear terminal: cls

# To Create a report of testcases:
#          Without Report Folder : pytest File_Name/testcase_Name -v --html=report.html
#             With Report Folder : pytest File_Name/testcase_Name -v --html=Report/report.html

# To run testcses parellely: pytest -n=4
# Install library for parallel run pytest-xdist
# Install library for reports pytest-html