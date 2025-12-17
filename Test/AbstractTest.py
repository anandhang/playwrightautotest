
import pytest
from Driver.DriverManager import DriverManager
from Infra.Reporter import TestReporter

class AbstractTest:
    driver = None
    page = None
    reporter = TestReporter()

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # Setup
        self.reporter.log_info("Starting Test Execution")
        self.page = DriverManager.get_driver("chrome") # Default to chrome, could be parameterized
        yield
        # Teardown
        self.reporter.log_info("Ending Test Execution")
        DriverManager.close_driver()
