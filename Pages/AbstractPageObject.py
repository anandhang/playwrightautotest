
from abc import ABC, abstractmethod

class AbstractPageObject(ABC):
    def __init__(self, page):
        self.page = page
        
    def get_page_title(self):
        return self.page.title()
    
    def get_url(self):
        return self.page.url
    
    def navigate_to(self, url):
        self.page.goto(url)
