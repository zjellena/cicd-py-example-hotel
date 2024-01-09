from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestHotel(object):
    def setup_method(self):
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome(service=service, options=options)
        URL = "http://hotel-v2.progmasters.hu/"
        self.browser.get(URL)
        self.browser.maximize_window()

    def teardown_method(self):
        self.browser.quit()

    def test_open(self):
        page_name = self.browser.find_element(By.ID, 'nav-index')
        assert page_name.is_displayed()
        assert page_name.text == "HOOTEL"

    def test_login(self):
        signin_btn = self.browser.find_element(By.CSS_SELECTOR, 'a[class="nav-link"]')
        signin_btn.click()
        email_input = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'email')))
        password_input = self.browser.find_element(By.ID, 'password')
        login_btn = self.browser.find_element(By.CSS_SELECTOR, 'button[name="submit"]')
        email_input.send_keys('andi.teszt2021@gmail.com')
        password_input.send_keys('tesztelek2021')
        login_btn.click()
        profile_id = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.ID, 'profile')))
        assert profile_id.text == "Profilom (Andrea)"