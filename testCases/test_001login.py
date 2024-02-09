from pageObjencts.LoginPage import LoginClass
from utilities.ReadConfigFile import Readconfig
from selenium import webdriver

import time

class Test_Login:

    Email1= Readconfig.getEmail()
    Password1= Readconfig.getPassword()

    def test_verify_url001(self, setup):
        self.driver=setup
        print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_fail.png")
            assert False
        self.driver.close()

    def test_user_login_002(self,setup):
        self.driver = setup
        self.lc=LoginClass(self.driver)
        self.lc.Enter_Email(self.Email1)
        self.lc.Enter_Password(self.Password1)
        self.lc.Click_Login()

        if self.lc.Verify_Login_Stauts() == "Login Pass":
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.lc.Click_Logout()
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False
        self.driver.close()