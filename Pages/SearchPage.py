from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.categories_menu = (By.LINK_TEXT, 'Categorías')

    def click_on_categories_menu(self):
        link = wait(self.driver, 5).until(EC.element_to_be_clickable(self.categories_menu))
        hover = ActionChains(self.driver).move_to_element(link)
        hover.perform()

    def click_on_sub_menu(self, text):
        element = self.driver.find_element_by_class_name('nav-menu')
        try:
            link = wait(element, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, text)))
            link.click()
        except TimeoutException:
            raise Exception('Category not found!')
