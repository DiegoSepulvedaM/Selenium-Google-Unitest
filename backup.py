"""Modules
    
    """

import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class TestGoogleSearch(unittest.TestCase):
    """
    Google Selenium Script

    This script uses Selenium to perform a Google search and capture the search results.

    Attributes:
        chromedriver_path (str): The path to the chromedriver executable.
        chrome_binary_path (str): The path to the Google Chrome binary.
        options (selenium.webdriver.chrome.options.Options): Chrome options for configuring the webdriver.
        chrome_service (selenium.webdriver.chrome.service.Service): Chrome service for configuring the webdriver.
        driver (selenium.webdriver.chrome.webdriver.WebDriver): Chrome webdriver instance.

    Methods:
        run_google_search(query):
            Performs a Google search with the provided query and captures the search results.

        main():
            Main entry point of the script.

    Example:
        To run the script, create an instance of the script and call the main() method:

        >>> google_script = GoogleSeleniumScript()
        >>> google_script.main()"""


def setUp(self):
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
    # Limpieza después de cada prueba
    self.driver.quit()


if __name__ == "__main__":
    unittest.main()