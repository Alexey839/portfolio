from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Создание экранов приложения:
class ScreenOne(Screen):
pass

class ScreenTwo(Screen):
pass

class ScreenThree(Screen):
pass

# Создание экземпляра менеджера экранов и добавление экранов:
sm = ScreenManager()
sm.add_widget(ScreenOne(name='screen_one'))
sm.add_widget(ScreenTwo(name='screen_two'))
sm.add_widget(ScreenThree(name='screen_three'))

# Создание основного класса приложения
class MyApp(App):

def build(self):
# Указание экрана, которое будет показываться в начале работы приложения
return sm

if __name__ == '__main__':
# Запуск приложения
MyApp().run()