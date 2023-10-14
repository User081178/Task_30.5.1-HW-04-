#30.5.1 В написанном тесте (проверка карточек питомцев) добавьте неявные ожидания всех элементов
# (фото, имя питомца, его возраст).

import pytest
from selenium.webdriver.common.by import By
from settings import valid_email, valid_password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#service = Service(executable_path='./chromedriver.exe')
#driver = webdriver.Chrome(service=service)

def test_pet_frends():
    """Проверка карточек питомцев всех пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Ввод эл.почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопке "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверка того, что осуществлен переход на главную страницу пользователя
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    # Три переменные, в которых записали все найденные элементы на странице:

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')


    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != '', 'SRC is missing !'
        assert names[i].text != '', 'Pet name is missing !'
        assert descriptions[i].text != '', 'There is no description ! '
        assert ',' in descriptions[i].text, 'Comma in description ! !'
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0