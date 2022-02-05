import pytest
from selenium import  webdriver
from pageobjects.LoginPage import LoginPage
from utilities.readproperties import ReadConfig
from utilities.customLogger import logGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = logGen.loggen()


    def test_login_ddt(self, setup):
        self.logger.info("*************Test_002_Login***************")
        self.logger.info("*************verify Login test_DDT***************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows= XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in excel",self.rows)

        list_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time. sleep(10)
            act_title = self.driver.title
            exp_title ="Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("Passed")
                    self.lp.clicklogout();
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Failed")
                    self.lp.clicklogout();
                    list_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("Failed")
                    self.lp.clicklogout()
                    list_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("Passed")
                    list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("Login DDt test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Logic data test is faile")
            self.driver.close()
            assert False
        self.logger.info("End of login DDT test")
        self.logger.info("completed test DDt")





