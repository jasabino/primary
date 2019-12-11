from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Pages.SearchPage import SearchPage
from Pages.ResultPage import ResultPage
from Pages.DetailPage import DetailPage
import pytest
import time


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.mercadolibre.com.ar/')
    yield driver
    driver.close()
    driver.quit()


#@pytest.mark.skip(reason='testing')
@pytest.mark.parametrize('category, subcategory', [('Hogar y Electrodomésticos', 'Climatización'),
                                                   ('Tecnología', 'Celulares y Smartphones'),
                                                   ('Belleza y Cuidado Personal', 'Perfumes Importados'),
                                                   ('Herramientas e Industria', 'Industria Textil'),
                                                   ('Juguetes y Bebés', 'Cuarto del Bebé')])
def test_categories_two_level(driver, category, subcategory):
    search_page = SearchPage(driver)
    result_page = ResultPage(driver)
    search_page.click_on_categories_menu()
    search_page.click_on_sub_menu(category)
    search_page.click_on_sub_menu(subcategory)
    title = result_page.get_title()
    results = result_page.get_total_results().split()

    assert title == subcategory or title == category
    assert int(results[0].replace('.', '')) > 0
    assert results[1] == 'resultados'


@pytest.mark.parametrize('category, subcategory, filter',  [('Tecnología', 'Celulares y Smartphones', 'Capital Federal')])
def test_filter_category(driver, category, subcategory, filter):
    search_page = SearchPage(driver)
    result_page = ResultPage(driver)
    detail_page = DetailPage(driver)
    search_page.click_on_categories_menu()
    search_page.click_on_sub_menu(category)
    search_page.click_on_sub_menu(subcategory)

    result_page.apply_filter(filter)

    item = result_page.get_random_item()
    data = result_page.get_data_item(item)
    result_page.click_on_item(item)
    data_detail = detail_page.get_data_item()

    assert data[0] == data_detail[0]
    assert data[1] == data_detail[1]


