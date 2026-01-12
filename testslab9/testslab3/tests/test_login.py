import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

BASE_URL = "http://localhost:5000"

@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_argument("--headless")                
    options.add_argument("--no-sandbox")             
    options.add_argument("--disable-dev-shm-usage")    
    options.add_argument("--disable-gpu")              
    options.add_argument("--window-size=1920,1080")    

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_browser_initialization_and_close(browser):
    """Проверка инициализации браузера, открытия страницы и закрытия."""
    browser.get(BASE_URL)
    assert "Login" in browser.title or browser.current_url.endswith("/login")

def test_valid_login(browser):
    """Ввод валидных credentials и проверка успешного входа."""
    browser.get(f"{BASE_URL}/login")
    
    browser.find_element(By.ID, "username").send_keys("admin")
    browser.find_element(By.ID, "password").send_keys("password123")
    browser.find_element(By.ID, "login-button").click()

    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "logout-link"))
    )

    logout_link = browser.find_element(By.ID, "logout-link")
    assert logout_link.is_displayed()
    assert logout_link.text == "Logout"
