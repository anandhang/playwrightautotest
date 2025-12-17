
from .BaseControl import BaseControl

class TextBox(BaseControl):
    def enter_text(self, text):
        self.get_element().fill(text)
    
    def get_text(self):
        return self.get_element().input_value()

class Button(BaseControl):
    pass  # Inherits click from BaseControl

class CheckBox(BaseControl):
    def check(self):
        if not self.is_checked():
            self.get_element().check()
            
    def uncheck(self):
        if self.is_checked():
            self.get_element().uncheck()
            
    def is_checked(self):
        return self.get_element().is_checked()

class ListBox(BaseControl):
    def select_by_value(self, value):
        self.get_element().select_option(value=value)
        
    def select_by_label(self, label):
        self.get_element().select_option(label=label)

class Grid(BaseControl):
    def get_row_count(self):
        return self.get_element().locator("tr").count()
        
    def get_cell_text(self, row_index, col_index):
        # Assuming standard HTML table structure
        return self.get_element().locator(f"tr:nth-child({row_index + 1}) td:nth-child({col_index + 1})").text_content()
