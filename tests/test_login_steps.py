from pytest_bdd import given,when,then,scenarios,parsers
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from playwright.sync_api import Page

scenarios('../tests/login.feature')

@given("the user is on login page")
def open_login_page(page:Page):
    login_page =LoginPage(page)
    login_page.navigate()
    

@when(parsers.parse("the user enters username as {username} and password as {password}"))
def enter_valid_cred(page:Page,user,password):
    login_page = LoginPage(page)
    login_page.enter_cred(user,password)
    

@when("the user clicks the login button")
def login_click(page:Page):
    page.click_login()
    
    
@then("the user should redirect to product page")
def succesfull_login(page:Page):
    page = ProductPage(page)
    page.verify_product_page()
    
@then("the user will see the error message")
def invalid_cred_error(page:Page):
    print("User can see error message")
    page = LoginPage(page)
    page.verify_login_error()
    
    