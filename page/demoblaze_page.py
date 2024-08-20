"""Aici scriem codul pentru pasii scrisi in limbajul Gherkin"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page.base_page import BasePage

class DemoBlazePage(BasePage):

    def click_login(self):
        self.chrome.find_element(By.ID, "login2").click()

    def input_username(self):
        input_user = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.ID, "loginusername")))
        input_user.send_keys("poprobert")

    def input_password(self):
        self.chrome.find_element(By.ID, "loginpassword").send_keys("poprobert321")

    def click_login_after_credentials(self):
        self.chrome.find_element(By.XPATH, '//button[@onclick="logIn()"]').click()

    def login_finished(self):
        WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.ID, "nameofuser")))
        user = self.chrome.find_element(By.ID, "nameofuser")
        assert user.text == "Welcome poprobert"

    def phone_category(self):
        phone = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.ID,"itemc")))
        phone.click()

    def press_samsung(self):
        phone = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.XPATH,'//img[@src="imgs/galaxy_s6.jpg"]')))
        phone.click()

    def press_add_to_cart(self):
        add_to_cart = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.XPATH,'//a[@onclick="addToCart(1)"]')))
        add_to_cart.click()
    def message_product_added(self):
        time.sleep(1)
        self.chrome.switch_to.alert.accept()

    def press_cart(self):
        cart = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.ID, "cartur")))
        cart.click()

    def verify_s6_samsung(self):
        s6 = WebDriverWait(self.chrome, 10).until(EC.visibility_of_element_located((By.XPATH,'// *[ @ id = "tbodyid"] / tr / td[2]')))
        assert s6.text == "Samsung galaxy s6"

    def place_order(self):
        self.chrome.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()

    def name_robert(self):
