import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class TestGoogleSearch(unittest.TestCase):
    """Test class to verify the functionality of Google Search.

    This class contains setup, test, and teardown methods to perform Google searches using Selenium.

    Attributes:
        chrome_service (webdriver.chrome.service.Service): ChromeDriver service for the test.
        driver (webdriver.chrome.webdriver.WebDriver): Instance of the Chrome browser for the test.
    """
    def setUp(self):
        """Set up before each test.

        Configures the Chrome service and WebDriver with specific options
        before running each test.
        """
        # Configuración antes de cada prueba
        chromedriver_path = "/usr/local/bin/chromedriver"
        chrome_binary_path = "/usr/local/bin/google-chrome"
        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument("--window-position=0,0")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        self.chrome_service = ChromeService(executable_path=chromedriver_path)
        self.driver = webdriver.Chrome(service=self.chrome_service, options=options)

    def test_google_search(self):
        """Test the Google Search functionality.

        Opens Google, performs a search with the word 'Diego', waits a few seconds
        to load the results, takes a screenshot, and verifies that 'Diego' is in the title.
        """
        # Prueba: Realiza una búsqueda en Google y verifica el título de la página
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element("name", "q")
        search_box.send_keys("Diego")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)
        screenshot_path = "google_search_results.png"
        self.driver.save_screenshot(screenshot_path)
        self.assertIn("Diego", self.driver.title)

    def tearDown(self):
        """Clean up after each test.

        Closes the Chrome browser after running each test.
        """
        # Limpieza después de cada prueba
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
