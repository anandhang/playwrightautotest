
from .AbstractTest import AbstractTest
from TestLogics.LoginLogic import LoginLogic

class TestLogin(AbstractTest):
    def test_valid_login(self):
        self.reporter.log_step("Initialize Login Logic")
        login_logic = LoginLogic(self.page)
        
        self.reporter.log_step("Perform Login")
        login_logic.perform_login("standard_user", "secret_sauce")
        
        # Simple assertion to verify login - checking url or title
        assert "inventory" in self.page.url
        self.reporter.log_info("Login Successful")
