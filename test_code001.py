import time
from nose.tools import assert_equal
from selenium import webdriver
import unittest
import HtmlTestRunner
from Digicampushybrid.Digicampusfunction.dlogin import loginpage
from Digicampushybrid.Digicampusfunction.dstaffdirectory import staff

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            "C:/Python27/chrome_exe/chromedriver_2.36.exe")
        cls.driver.get("http://localhost/projects/school_new/site/login")
        cls.driver.maximize_window()

    def test_a_login_fun(self):
        driver = self.driver
        login = loginpage(driver)
        login.enter_username("admin@admin.com")
        login.enter_password("1zz2xx3cc")
        login.click_submit()
        assert_equal(driver.title, "Your School Name")
        time.sleep(2)

    def test_b_staffdirectory(self):
        driver = self.driver
        staffdirectory = staff(driver)
        staffdirectory.staff_directory()

    def test_c_staff_add(self):
        driver = self.driver
        add = staff(driver)
        add.staff_add()

    def test_d_staff_input(self):
            driver = self.driver
            input = staff(driver)
            input.staff_input()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report'))


