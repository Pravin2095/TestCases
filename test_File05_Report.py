
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service

Chrome_Options = webdriver.ChromeOptions()
Chrome_Options.add_argument("headless")
Service_Object = Service()

# To make a report install library pytest html.

import pytest

class TestCase_Credence:


    def test_Credence_Logo(self):

        Driver = webdriver.Chrome(options = Chrome_Options)
        Driver.get("https://credence.in")

        Driver.implicitly_wait(30)

        Logo = Driver.find_element(By.XPATH,"//title[normalize-space()='Credence']").is_displayed()

        print(Driver.title)                          # "title" is display page title.
                                                     # It is another way to check reach currectly on page.
        if Driver.title == "Credence":
            assert True
        else:
            assert False


    def test_Credence_Number(self):

        Driver = webdriver.Chrome(options = Chrome_Options)
        Driver.get("https://credence.in")

        Driver.implicitly_wait(30)

        Driver.find_element(By.XPATH,"//img[@src='/website/images/enquiry.png']").click()

        l = len(Driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a"))
        print(l)

        List = []
        for p in range(1,l+1):

            Number = Driver.find_elements(By.XPATH,"//div[@class='quickfinder-description gem-text-output']//p//a["+str(p)+"]")
            print(p)

            List.append(Number)

        if '+91 9579064658'in List:
              assert True

        # else:
        #       assert False


    # Report Remaining:
    # library installation


# pytest test_File05_Report.py -v --html=Report/report.html