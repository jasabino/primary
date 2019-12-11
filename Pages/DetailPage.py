from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class DetailPage:
    def __init__(self, driver):
        self.driver = driver

    def get_data_item(self):
        desc = wait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-pdp-title')))[0].text
        price = wait(self.driver, 5).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'price-tag-fraction')))[0].text
        return [desc, price]



