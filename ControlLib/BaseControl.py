
from abc import ABC, abstractmethod

class BaseControl(ABC):
    def __init__(self, page, xpath):
        self.page = page
        self.xpath = xpath

    def get_element(self):
        return self.page.locator(self.xpath)
    
    def is_visible(self):
        return self.get_element().is_visible()
    
    def click(self):
        self.get_element().click()
