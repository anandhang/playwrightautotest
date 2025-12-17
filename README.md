# Playwright Automation Framework (Python + OOP + POM)

## Overview
This project is a scalable and modular UI automation framework built using **Python** and **Playwright**. It strictly follows **Object-Oriented Programming (OOP)** principles and the **Page Object Model (POM)** design pattern to ensure maintainability and reusability.

## Key Features
- **Page Object Model (POM)**: Separation of page objects (locators & behaviors) from test logic.
- **Control Library**: Custom wrappers for UI controls (TextBox, Button, Grid, etc.) for consistent interaction.
- **Driver Management**: Centralized driver factory supporting Chrome, Firefox, and Edge.
- **Separation of Concerns**: Distinct layers for Infrastructure, Controls, Pages, Logic, and Tests.
- **Reporting**: Integrated logging and reporting mechanism.
- **Cross-Browser Support**: Easily switch between browsers via configuration.

## Project Structure

```
playwrightautotest/
├── ControlLib/       # Custom UI Control wrappers (BaseControl, TextBox, etc.)
├── Driver/           # Browser factory and implementations (Chrome, Firefox, Edge)
├── Infra/            # Infrastructure utilities (Reporter, ConfigReader)
├── Pages/            # Page representations (Locators & Page Actions)
├── TestLogics/       # Business Logic & Workflows (orchestrating multiple pages)
├── TEST/             # Test Cases (Pytest)
├── reports/          # Execution logs and reports
├── config.json       # (Optional) Configuration file
└── README.md         # Project Documentation
```

## Prerequisites
- Python 3.8+
- Playwright

## Installation

1.  **Clone the repository** (if applicable) or download the source.
2.  **Install Dependencies**:
    ```bash
    pip install pytest pytest-html playwright
    ```
3.  **Install Playwright Browsers**:
    ```bash
    playwright install
    ```

## Usage

### 1. Running Tests
Run all tests using `pytest`:
```bash
python -m pytest TEST/
```

Run a specific test file:
```bash
python -m pytest TEST/test_login.py
```

Generate an HTML Report:
```bash
python -m pytest TEST/ --html=reports/report.html
```

### 2. Creating a New Test

**Step 1: Create a Page Object**
Create a new class in `Pages/` inheriting from `AbstractPageObject`.
```python
from .AbstractPageObject import AbstractPageObject
from ControlLib.Controls import TextBox, Button

class LoginPage(AbstractPageObject):
    def __init__(self, page):
        super().__init__(page)
        self.username = TextBox(page, "//input[@id='user']")
        self.submit = Button(page, "//button[@id='login']")
```

**Step 2: Create Test Logic (Optional but Recommended)**
Create a logic class in `TestLogics/` to handle workflows.
```python
from Pages.LoginPage import LoginPage

class LoginLogic:
    def __init__(self, page):
        self.login_page = LoginPage(page)

    def login(self, user, pwd):
        self.login_page.username.enter_text(user)
        self.login_page.submit.click()
```

**Step 3: Create the Test Case**
Create a test file in `TEST/` inheriting from `AbstractTest`.
```python
from .AbstractTest import AbstractTest
from TestLogics.LoginLogic import LoginLogic

class TestMyApp(AbstractTest):
    def test_login_flow(self):
        logic = LoginLogic(self.page)
        logic.login("admin", "1234")
```

## Components Description

- **ControlLib**: Abstract `BaseControl` and concrete implementations like `TextBox`, `ListBox`, `CheckBox`. Usage: `TextBox(page, xpath_selector)`.
- **Driver**: `DriverManager` singleton for managing browser instances.
- **Infra**: `TestReporter` for logging steps and errors.
