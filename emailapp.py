import smtplib
from email.message import EmailMessage

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Login(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text = "Username: "))
        self.userInput = TextInput(multiline = False)
        self.add_widget(self.userInput)

        self.add_widget(Label(text = "Password: "))
        self.passInput = TextInput(multiline = False)
        self.add_widget(self.passInput)

        self.add_widget(Label(text = ""))

        self.loginButton = Button(text = "Log in")
        self.loginButton.bind(on_press = self.login)
        self.add_widget(self.loginButton)

    def login(self, instance):
        self.email = self.userInput.text
        self.password = self.passInput.text

        email_app.screen_manager.current = "email_page"

    
class EmailPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text = "To: "))

        self.to = TextInput()
        self.add_widget(self.to)

        self.add_widget(Label(text = "Subject: "))

        self.subject = TextInput()
        self.add_widget(self.subject)

        self.add_widget(Label(text = "Message: "))

        self.message = TextInput()
        self.add_widget(self.message)

        self.send_msg = Button(text = "Send")
        self.send_msg.bind(on_press = self.send_email)
        self.add_widget(self.send_msg)

    def send_email(self, instance):
        EMAIL_ADDRESS = email_app.login.email
        EMAIL_PASSWORD = email_app.login.password

        msg = EmailMessage()
        msg['Subject'] = self.subject.text
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = self.to.text

        msg.set_content(self.message.text)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


class EmailApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.login = Login()
        screen = Screen(name = "login_page")
        screen.add_widget(self.login)
        self.screen_manager.add_widget(screen)

        self.email_page = EmailPage()
        screen = Screen(name = "email_page")
        screen.add_widget(self.email_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

if __name__ == "__main__":
    email_app = EmailApp()
    email_app.run()