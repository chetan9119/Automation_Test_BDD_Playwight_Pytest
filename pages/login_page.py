from playwright.sync_api import Page #type:ignore

class LoginPage:
    def __init__(self, page:Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_btn = page.get_by_role("button", name = "Login")
        self.failed_login = page.locator("button.error-button")
        
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")
        
    def enter_cred(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        
    def click_login(self):
        self.login_btn.click()
        
    def verify_login_error(self):
        self.failed_login.is_visible()
  
        