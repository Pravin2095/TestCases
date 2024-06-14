from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
Service_Object = Service()


class TestCase_Headless:

    def test_YouTube(self):

        Driver = webdriver.Chrome(options = chrome_options)
        Driver.get("https://www.youtube.com/")

        # Driver.implicitly_wait(10)

        Logo = Driver.find_element(By.XPATH,"//ytd-topbar-logo-renderer[@id='logo']").is_displayed()
        print(Logo)

        if Logo == True:
            assert True
        else:
            assert False


    def test_Google(self):

        Driver = webdriver.Chrome(options = chrome_options)
        Driver.get("https://www.google.co.in/")

        Image = Driver.find_element(By.XPATH,"//img[@alt='Google']").is_displayed()
        print(Image)

        if Image == True:
            assert True
        else:
            assert False


    def test_Facebook(self):

        Driver = webdriver.Chrome(options = chrome_options)
        Driver.get("https://www.facebook.com")

        Title = Driver.find_element(By.XPATH,"//img[@alt='Facebook']").is_displayed()
        print(Title)

        if Title == True:
            assert True
        else:
            assert False



# Program or test case run in terminal also :
#                                              Use : pytest    (For run program and testcase)
#                                    More Detailed : pytest -v (For more detailed way to run program and testcase)

