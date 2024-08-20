"""Aici putem regasii pasii scrisi in limbajul Gherkin din fisierul js_alerts.features in pachetul python features"""
from behave import *
#Aici putem regasii pasii scrisi in limbajul Gherkin din fisierul js_alerts.features in pachetul python features
@given(u'I am on the main page')
def step_impl(context):
    print(u'STEP: Given I am on the main page')


@when(u'I press on the "Sign in" button')
def step_impl(context):
    print(u'STEP: When I press on the "Sign in" button')


@when(u'I input in the username field "poprobert"')
def step_impl(context):
    print(u'STEP: When I input in the username field "poprobert"')


@when(u'I input in the password field "poprobert321"')
def step_impl(context):
    print(u'STEP: When I input in the password field "poprobert321"')


@when(u'I press on the "Log in" button')
def step_impl(context):
    print(u'STEP: When I press on the "Log in" button')


@then(u'I should be signed in successfully')
def step_impl(context):
    print(u'STEP: Then I should be signed in successfully')


@when(u'I press on the "Phones" category')
def step_impl(context):
    print(u'STEP: When I press on the "Phones" category')


@when(u'I press on the "Samsung Galaxy s6"')
def step_impl(context):
    print(u'STEP: When I press on the "Samsung Galaxy s6"')


@when(u'I press on the "Add to cart" button')
def step_impl(context):
    print(u'STEP: When I press on the "Add to cart" button')


@then(u'I should see a message "Product added"')
def step_impl(context):
    print(u'STEP: Then I should see a message "Product added"')


@then(u'I press on the "OK" button in the alert pop-up')
def step_impl(context):
    print(u'STEP: Then I press on the "OK" button in the alert pop-up')


@then(u'I press on the "Cart" link')
def step_impl(context):
    print(u'STEP: Then I press on the "Cart" link')


@then(u'I should see the "Samsung Galaxy s6" in my cart')
def step_impl(context):
    print(u'STEP: Then I should see the "Samsung Galaxy s6" in my cart')


@then(u'I press on the "Place Order" button')
def step_impl(context):
    print(u'STEP: Then I press on the "Place Order" button')


@then(u'I input in the "Name" field "Robert"')
def step_impl(context):
    print(u'STEP: Then I input in the "Name" field "Robert"')


@then(u'I input in the "Country" field "Romania"')
def step_impl(context):
    print(u'STEP: Then I input in the "Country" field "Romania"')


@then(u'I input in the "City" field "Brasov"')
def step_impl(context):
    print(u'STEP: Then I input in the "City" field "Brasov"')


@then(u'I input in the "Credit card" field "123456789"')
def step_impl(context):
    print(u'STEP: Then I input in the "Credit card" field "123456789"')


@then(u'I input in the "Month" field "8"')
def step_impl(context):
    print(u'STEP: Then I input in the "Month" field "8"')


@then(u'I input in the "Year" field "2024"')
def step_impl(context):
    print(u'STEP: Then I input in the "Year" field "2024"')


@then(u'I press on the "Purchase" button')
def step_impl(context):
    print(u'STEP: Then I press on the "Purchase" button')


@then(u'I should see a confirmation pop-up with the order ID, amount paid, card number, name, and date')
def step_impl(context):
    print(u'STEP: Then I should see a confirmation pop-up with the order ID, amount paid, card number, name, and date')


@then(u'I press on the "OK" button')
def step_impl(context):
    print(u'STEP: Then I press on the "OK" button')
