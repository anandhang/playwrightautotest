
import json
import os

class ConfigReader:
    @staticmethod
    def read_config():
        # Assuming a config.json in the root for simplicity, or default values
        config_path = "config.json"
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f)
        else:
            # Default config
            return {
                "browser": "chrome",
                "headless": False,
                "base_url": "https://www.example.com"
            }
