Sprint_6
UI tests for Яндекс Самокат

data.py - набот тестовых данных:
class Url - список url страниц
class MainPageAnswers - ответы на вопросы блока Вопросы о важном
class UserOne - валидные данные пользователя один
class UserTwo - валидные данные пользователя два

conftest.py - фикстура:
def driver - настройки драйвера
def cookies - открыть главную страницу Самокат, принять куки

tests - сценарии, покрытые тестами:
test_main_page_question.py
def test_main_page_question - Проверка соответствия вопроса и ответа из выпадающего списка "Вопросы о важном"

test_main_page_switch.py
def test_scooter_logo - перенаправление на главную страницу "Яндекс Самокат" при клике на лого "Самокат"
def test_dzen_logo - перенаправление на главную страницу "Дзен" при клике на лого "Яндекс"

test_page_order_scooter.py
def test_order_header_button - создать заказ через кнопку "Заказать" в хедере
def test_order_middle_button - создать заказ через кнопку "Заказать" в середине страницы

Для запуска:
pip3 install -r requirements.txt - установить зависимости

pytest tests --alluredir=allure_results - запустить все тесты из директории tests

allure serve allure_results - посмотреть отчет