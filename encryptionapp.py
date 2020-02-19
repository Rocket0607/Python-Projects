import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivymd.theming import ThemeManager

class Home(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text = 'Would you like to encrypt or decrypt a message?', font_size = 25))
        self.e = Button(text = 'Encrypt', background_color = (72/ 255, 219 / 255, 251 / 255,1.0))
        self.e.bind(on_press = self.gotoencrypt )
        self.add_widget(self.e)
        self.d = Button(text = 'Decrypt', background_color = (255 / 255, 107 / 255, 107 / 255,1.0))
        self.d.bind(on_press = self.gotodecrypt)
        self.add_widget(self.d)
    
    def gotoencrypt(self, instance):
        eapp.screen_manager.current = 'encryptpage'
    def gotodecrypt(self, instance):
        eapp.screen_manager.current = 'decryptpage'

class EncryptPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.encryptbox = TextInput()
        self.add_widget(self.encryptbox)
        self.encryptbutton = Button(text = 'Encrypt')
        self.encryptbutton.bind(on_press = self.encrypt)
        self.add_widget(self.encryptbutton)
        self.backbutton = Button(text = 'Back')
        self.backbutton.bind(on_press = self.eback)
        self.add_widget(self.backbutton)

    def encrypt(self, instance):
        word = self.encryptbox.text
        eword = ''
        for letter in word:
            num = ord(letter)
            num = num + 3
            eword = eword + (chr(num))
            self.encryptbox.text = ''
        self.ewordl = TextInput(text = eword, font_size = 20)
        self.add_widget(self.ewordl)
    
    def eback(self, instance):
        eapp.screen_manager.current = 'home'
        try:
            self.remove_widget(self.ewordl)
        except Exception:
            pass
        self.encryptbox.text = ''



class DecryptPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.decryptbox = TextInput()
        self.add_widget(self.decryptbox)
        self.decryptbutton = Button(text = 'Decrypt')
        self.decryptbutton.bind(on_press = self.decrypt)
        self.add_widget(self.decryptbutton)
        self.backbutton = Button(text = 'Back')
        self.backbutton.bind(on_press = self.dback)
        self.add_widget(self.backbutton)

    def decrypt(self, instance):
        let = self.decryptbox.text
        dword = ''
        
        for lett in let:
            numb = ord(lett)
            numb = numb - 3
            dword = dword + ((chr(numb)))
            self.decryptbox.text = ''
        self.dwordl = TextInput(text = dword, font_size = 20)
        self.add_widget(self.dwordl)

    def dback(self, instance):
        eapp.screen_manager.current = 'home'
        try:
            self.remove_widget(self.dwordl)
        except Exception:
            pass

        self.decryptbox.text = ''


class EncryptApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.home = Home()
        screen = Screen(name = 'home')
        screen.add_widget(self.home)
        self.screen_manager.add_widget(screen)

        self.encryptpage = EncryptPage()
        screen = Screen(name = 'encryptpage')
        screen.add_widget(self.encryptpage)
        self.screen_manager.add_widget(screen)

        self.decryptpage = DecryptPage()
        screen = Screen(name = 'decryptpage')
        screen.add_widget(self.decryptpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


        
if __name__ == "__main__":
    eapp = EncryptApp()
    eapp.run()