from selenium import webdriver
from time import sleep
from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(2)
        btn_cookies = self.driver.find_element_by_xpath(
            '//*[@id="q-1330521921"]/div/div[2]/div/div/div[1]/div[1]/button')
        if(btn_cookies.is_displayed()):
            btn_cookies.click()
        btn_inicio = self.driver.find_element_by_xpath(
            '//*[@id="q-1330521921"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]')
        if(btn_inicio.is_displayed()):
            btn_inicio.click()
        """ Ingresar utilizando gmail """
        btn_login_chrome = self.driver.find_element_by_xpath(
            '//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        if(btn_login_chrome.is_displayed()):
            btn_login_chrome.click()
        """ Ingresar utilizando gmail """
        btn_login_facebook = self.driver.find_element_by_xpath(
            '//*[@id="q1236064299"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        if(btn_login_facebook.is_displayed()):
            btn_login_facebook.click()

        """ Cambio de pantalla """
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        """ Ingreso de usuario y contraseña """
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)
        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)
        btn_login = self.driver.find_element_by_xpath('//*[@id="u_0_0_0S"]')
        btn_login.click()

        """ Cambio a la pantalla principal"""
        self.driver.switch_to.window(base_window)

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button')
        if(like_btn.is_displayed()):
            like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="q-1330521921"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button')
        if(dislike_btn.is_displayed()):
            dislike_btn.click()


""" Secuencia de ejecución """
bot = TinderBot()
""" bot.login() """
