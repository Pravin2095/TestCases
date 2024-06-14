from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
Service_Object = Service()

import pytest                           # It is for impose marker on testcases.

class Test_Cases:                       # Class name must be in Capital latter otherwise it's showed 'Empty Suit

    @pytest.mark.Arithmatic
    @pytest.mark.skip
    def test_Addition(self):
        A = 50
        B = 150
        Addition = A + B
        print(Addition)

        if Addition == 200:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    @pytest.mark.xfail
    def test_Minus(self):
        C = 450
        D = 135
        Minus = C - D
        print(Minus)

        if Minus == 315:
            print("Test Case id Passed")
        else:
            print("Test Case id Failed")

    @pytest.mark.Arithmatic
    def test_Multi(self):
        A = 25
        B = 12
        Multi = A * B
        print(Multi)

        if Multi == 300:
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


    def test_String(self):
        Name = "Pravin Vinayak Ingle"
        print(Name)

        if "Pravin" in Name:
            assert True
        else:
            assert False


    def test_List(self):

        List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        print(List)

        if 11 in List:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_YouTube(self):

        Driver = webdriver.Chrome(options=chrome_options)
        Driver.get("https://www.youtube.com/")

        # Driver.implicitly_wait(10)

        Logo = Driver.find_element(By.XPATH, "//ytd-topbar-logo-renderer[@id='logo']").is_displayed()
        print(Logo)

        if Logo == True:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_Google(self):

        Driver = webdriver.Chrome(options=chrome_options)
        Driver.get("https://www.google.co.in/")

        Image = Driver.find_element(By.XPATH, "//img[@alt='Google']").is_displayed()
        print(Image)

        if Image == True:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_Facebook(self):

        Driver = webdriver.Chrome(options=chrome_options)
        Driver.get("https://www.facebook.com")

        Title = Driver.find_element(By.XPATH, "//img[@alt='Facebook']").is_displayed()
        print(Title)

        if Title == True:
            assert True
        else:
            assert False

    @pytest.mark.skip
    def test_Instagram(self):

        Driver = webdriver.Chrome(options = chrome_options)
        Driver.get("https://www.instagram.com/")

        Name = Driver.find_element(By.XPATH,"//i[@aria-label='Instagram']").is_displayed()
        print(Name)

        if Name == True:
            assert True
        else:
            assert False


# Python mark on specific testcase mark like skip,xfail and make specific section of testcases.
# To run specific group of testcase in terminal:
#                                               pytest -v -m Group_Name

