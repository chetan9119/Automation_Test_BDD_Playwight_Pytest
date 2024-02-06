
Feature: User Login

Scenario: Successfull login with valid credentials
    Given: the user is on login page
    When: the user enters username as "standard_user" and password as "secret_sauce"
    And: the user clicks the login button
    Then: the user should redirect to product page


Scenario: Login with invalid credentials
    Given: the user is on login page
    When: the user enters username as "user" and password as "pass"
    And: the user clicks the login button
    Then: the user will see the error message