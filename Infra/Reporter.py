
import logging
import os
from datetime import datetime

class TestReporter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TestReporter, cls).__new__(cls)
            cls._instance.setup_logger()
        return cls._instance

    def setup_logger(self):
        log_dir = "reports"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(log_dir, f"test_execution_{timestamp}.log")
        
        self.logger = logging.getLogger("TestReporter")
        self.logger.setLevel(logging.INFO)
        
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        # Also log to console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_step(self, message):
        self.logger.info(f"STEP: {message}")
