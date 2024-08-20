from page.base_page import BasePage
from browser import Browser
from page.demoblaze_page import DemoBlazePage

def before_all(context):
    context.browser = Browser()
    context.base_page = BasePage()
    context.demoblaze_page = DemoBlazePage()

def after_all(context):
    context.browser.close()