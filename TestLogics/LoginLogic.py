
from Pages.LoginPage import LoginPage

class LoginLogic:
    def __init__(self, page):
        self.login_page = LoginPage(page)

    def perform_login(self, username, password):
        # Additional logic can be added here, e.g., checking if already logged in
        self.login_page.navigate_to("https://www.saucedemo.com/")
        self.login_page.do_enter_username(username)
        self.login_page.do_enter_password(password)
        self.login_page.do_click_loginbtn()
        # Could return a DashboardPage object or similar
