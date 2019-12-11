from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class ResultPage:
    def __init__(self, driver):
        self.driver = driver
        self.title_class = (By.CLASS_NAME, 'breadcrumb__title')
        self.results_class = (By.CLASS_NAME, 'quantity-results')

    def get_title(self):
        title = wait(self.driver, 5).until(EC.presence_of_element_located(self.title_class))
        return title.text

    def get_total_results(self):
        results = wait(self.driver, 5).until(EC.presence_of_element_located(self.results_class))
        return results.text

    def apply_filter(self, text):
        element = self.driver.find_element_by_class_name('filters__groups')
        filter = wait(element, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
        filter.click()

    def get_random_item(self):
        elements = self.driver.find_elements_by_class_name('item__info-container')
        random_num = randint(1, len(elements))
        return elements[random_num]

    def get_data_item(self, item):
        desc = item.find_element_by_class_name('main-title').text
        price = item.find_element_by_class_name('price__fraction').text
        return [desc, price]

    def click_on_item(self, item):
        item.find_element_by_class_name('item__info-title').click()

