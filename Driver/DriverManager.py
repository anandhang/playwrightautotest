
from playwright.sync_api import sync_playwright
from abc import ABC, abstractmethod

class BrowserFactory(ABC):
    @abstractmethod
    def create_browser(self, playwright):
        pass

class ChromeFactory(BrowserFactory):
    def create_browser(self, playwright):
        return playwright.chromium.launch(headless=False)

class FirefoxFactory(BrowserFactory):
    def create_browser(self, playwright):
        return playwright.firefox.launch(headless=False)

class EdgeFactory(BrowserFactory):
    def create_browser(self, playwright):
        return playwright.chromium.launch(channel="msedge", headless=False)

class DriverManager:
    _playwright = None
    _browser = None
    _page = None

    @staticmethod
    def get_driver(browser_name="chrome"):
        if DriverManager._page is None:
            DriverManager._playwright = sync_playwright().start()
            
            factory = None
            if browser_name.lower() == "chrome":
                factory = ChromeFactory()
            elif browser_name.lower() == "firefox":
                factory = FirefoxFactory()
            elif browser_name.lower() == "edge":
                factory = EdgeFactory()
            else:
                raise ValueError(f"Unsupported browser: {browser_name}")
            
            DriverManager._browser = factory.create_browser(DriverManager._playwright)
            DriverManager._page = DriverManager._browser.new_page()
            
        return DriverManager._page

    @staticmethod
    def close_driver():
        if DriverManager._browser:
            DriverManager._browser.close()
            DriverManager._browser = None
        if DriverManager._playwright:
            DriverManager._playwright.stop()
            DriverManager._playwright = None
        DriverManager._page = None
