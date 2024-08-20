"""Aici scriem clasa BasePage care o sa ne ajute sa navigam pe pagina principala"""
from browser import Browser

class BasePage(Browser):
    def navigate_to_main_page(self):
        self.chrome.get("https://www.demoblaze.com")
