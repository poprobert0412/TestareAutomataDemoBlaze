Feature: Test the DemoBlaze website

  Background:
    Given I am on the main page

  Scenario: Sign in
    When I press on the "Sign in" button
    And I input in the username field "poprobert"
    And I input in the password field "poprobert321"
    And I press on the "Log in" button
    Then I should be signed in successfully

  Scenario: Adding a phone into the cart and placing the order
    When I press on the "Phones" category
    And I press on the "Samsung Galaxy s6"
    And I press on the "Add to cart" button
    Then I should see a message "Product added"
    And I press on the "OK" button in the alert pop-up
    And I press on the "Cart" link
    Then I should see the "Samsung Galaxy s6" in my cart
    And I press on the "Place Order" button
    And I input in the "Name" field "Robert"
    And I input in the "Country" field "Romania"
    And I input in the "City" field "Brasov"
    And I input in the "Credit card" field "123456789"
    And I input in the "Month" field "8"
    And I input in the "Year" field "2024"
    And I press on the "Purchase" button
    Then I should see a confirmation pop-up with the order ID, amount paid, card number, name, and date
    And I press on the "OK" button
