"""Aici putem regasii pasii scrisi in limbajul Gherkin din fisierul demoblaze.features in pachetul python features"""
from behave import *
#Aici putem regasii pasii scrisi in limbajul Gherkin din fisierul js_alerts.features in pachetul python features
@given(u'I am on the main page')
def step_impl(context):
    print(u'STEP: Given I am on the main page')
    context.base_page.navigate_to_main_page()

@when(u'I press on the "Log in" button')
def step_impl(context):
    print(u'STEP: When I press on the "Sign in" button')
    context.demoblaze_page.click_login()

@when(u'I input in the username field "poprobert"')
def step_impl(context):
    print(u'STEP: When I input in the username field "poprobert"')
    context.demoblaze_page.input_username()

@when(u'I input in the password field "poprobert321"')
def step_impl(context):
    print(u'STEP: When I input in the password field "poprobert321"')
    context.demoblaze_page.input_password()

@when(u'I press on the "Log in" button after credentials')
def step_impl(context):
    print(u'STEP: When I press on the "Log in" button after credentials')
    context.demoblaze_page.click_login_after_credentials()

@then(u'I should be signed in successfully')
def step_impl(context):
    print(u'STEP: Then I should be signed in successfully')
    context.demoblaze_page.login_finished()


@when(u'I press on the "Phones" category')
def step_impl(context):
    print(u'STEP: When I press on the "Phones" category')
    context.demoblaze_page.phone_category()

@when(u'I press on the "Samsung Galaxy s6"')
def step_impl(context):
    print(u'STEP: When I press on the "Samsung Galaxy s6"')
    context.demoblaze_page.press_samsung()

@when(u'I press on the "Add to cart" button')
def step_impl(context):
    print(u'STEP: When I press on the "Add to cart" button')
    context.demoblaze_page.press_add_to_cart()

@when(u'I press on the "OK" button in the alert pop-up')
def step_impl(context):
    print(u'STEP: Then I press on the "OK" button in the alert pop-up')
    context.demoblaze_page.message_product_added()

@when(u'I press on the "Cart" link')
def step_impl(context):
    print(u'STEP: Then I press on the "Cart" link')
    context.demoblaze_page.press_cart()

@then(u'I should see the "Samsung Galaxy s6" in my cart')
def step_impl(context):
    print(u'STEP: Then I should see the "Samsung Galaxy s6" in my cart')
    context.demoblaze_page.verify_s6_samsung()

@then(u'I press on the "Place Order" button')
def step_impl(context):
    print(u'STEP: Then I press on the "Place Order" button')
    context.demoblaze_page.place_order()

@then(u'I input in the "Name" field "Robert"')
def step_impl(context):
    print(u'STEP: Then I input in the "Name" field "Robert"')
    context.demoblaze_page.name_robert()

@then(u'I input in the "Country" field "Romania"')
def step_impl(context):
    print(u'STEP: Then I input in the "Country" field "Romania"')
    context.demoblaze_page.country()

@then(u'I input in the "City" field "Brasov"')
def step_impl(context):
    print(u'STEP: Then I input in the "City" field "Brasov"')
    context.demoblaze_page.city()

@then(u'I input in the "Credit card" field "1234567891011"')
def step_impl(context):
    print(u'STEP: Then I input in the "Credit card" field "1234567891011"')
    context.demoblaze_page.credit_card()

@then(u'I input in the "Month" field "8"')
def step_impl(context):
    print(u'STEP: Then I input in the "Month" field "8"')
    context.demoblaze_page.month()

@then(u'I input in the "Year" field "2028"')
def step_impl(context):
    print(u'STEP: Then I input in the "Year" field "2028"')
    context.demoblaze_page.year()

@then(u'I press on the "Purchase" button')
def step_impl(context):
    print(u'STEP: Then I press on the "Purchase" button')
    context.demoblaze_page.purchase_button()

@then(u'I should see a confirmation pop-up and press the "OK" button')
def step_impl(context):
    print(u'STEP: I should see a confirmation pop-up and press the "OK" button')
    context.demoblaze_page.ok_button()
