from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException, TimeoutException

URL = "http://localhost:5000/login"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    print(f" Открываем страницу: {URL}")
    driver.get(URL)
    
    title = driver.title
    print(f" Заголовок страницы: '{title}'")
    
except (WebDriverException, TimeoutException) as e:
    print(f" Ошибка при загрузке страницы: {e}")
    title = None

finally:
    print(" Закрываем браузер...")
    driver.quit()
    print(" Браузер успешно закрыт.")