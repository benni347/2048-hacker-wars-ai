#!/usr/bin/python
"""This is the main script"""
running = True
class Main():
    def init(self):
        self.x = 0
        self.start()
    
    def start(self):
        self.selected_browser = "firefox"
        print("Hello\nSelect one browser below\n1) Firefox\n2) Chrome\n")
        d = input()
        if d == "1":
           self.selected_browser = "firefox"
        elif d == "2":
            self.selected_browser = "chrome"
        else:
            print("You didn't enter a valid number")
            self.start()
        self.start_browser(self.selected_browser)

    def start_browser(self, browser):
        print(browser)

while running is True:
    main = Main().init()
    main
