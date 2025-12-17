
from .AbstractPageObject import AbstractPageObject
from ControlLib.Controls import TextBox, Button

class LoginPage(AbstractPageObject):
    def __init__(self, page):
        super().__init__(page)
        # Initialize controls with their xpaths
        self.username_txt = TextBox(page, "//input[@id='user-name']")
        self.password_txt = TextBox(page, "//input[@id='password']")
        self.login_btn = Button(page, "//input[@id='login-button']")
    
    def do_enter_username(self, username):
        self.username_txt.enter_text(username)

    def do_enter_password(self, password):
        self.password_txt.enter_text(password)

    def do_click_loginbtn(self):
        self.login_btn.click()