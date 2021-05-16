# Создание и запуск приложения, программирование интерфейса экранов и действий на них

# Здесь должен быть твой код
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.app import App
from kivy.app import App
from ruffier import index_ryf, test_ryf
name = " "
v = " "
x1 = " "
x2 = " "
x3 = " "



class ScrButton(Button):
    def __init__(self, screen, direction = 'right', 
    goal = 'main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
    pass
class MainScr(Screen):
    def __init__(self, name = 'main'):
        super().__init__(name = name)
        self.txt1 = Label(text = 'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья. \n Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работаспособности сердца при физической нагрузке.\n У ипытуемого определяют частоту пульса за 15 секунд. \n Затем в течение 45 секунд испытуемый выполняет 30 приседаний \n После оканчания нагрузки пульс подсчитывается вновь: число пульсаций за первые 15 секунд , 30 секунд отдыха, число пульсаций за последние 15 секунд.',markup=True, size_hint_y=None, font_size='18sp', halign='left', valign='top')
        self.inp1 = TextInput(multiline = False, text = 'Введите имя:', size_hint_y = None, font_size = '24sp')
        self.inp2 = TextInput(multiline = False, text = 'Введите возраст:', size_hint_y = None, font_size = '24sp' )
        btn1 = Button(text = 'Начать', size_hint_y = None, font_size = '24sp')
        #btn2 = ScrButton(self, "left", "second", text = '2', height = '30sp') 
       # btn3 = ScrButton(self, "up", "third", text = '3', height = '30sp')
        #btn4 = ScrButton(self, "down", "fourth", text = '4', height = '30sp')
        btn1.on_press = self.next
        self.scroll =ScrollView(size_hint = (1, 1))
        self.scroll.add_widget(self.txt1)
        self.txt1.bind(size = self.resize)
        layout = BoxLayout(orientation = "vertical" )
        layout.add_widget(self.scroll)
        layout.add_widget(self.inp1)
        layout.add_widget(self.inp2)
        layout.add_widget(btn1)
        #layout.add_widget(btn4)
        self.add_widget(layout)
    def resize(self,width,heid):
        self.txt1.text_size = (self.txt1.width, None)
        self.txt1.texture_update()
        self.txt1.height = self.txt1.texture_size[1]
    def next(self):
        global name, v
        name = self.inp1.text
        v = self.inp2.text
        self.manager.transition.direction = "left"
        self.manager.current = "first"

class FirstScr(Screen):
    def __init__(self, name = 'first'):
        super().__init__(name = name)
        self.txt = Label(text = 'Замерьте пульс за 15 секунд.\n Результат запишите в соответствующее поле.', markup=True, size_hint_y=None, font_size='18sp', halign='left', valign='top')
        
        self.inp = TextInput(multiline = False, text = 'Введите результат:', size_hint_y = None, font_size = '24sp')
        btn = Button(text = "Продолжить", size_hint_y = None, font_size = '24sp')
        btn.on_press = self.next
        self.scroll =ScrollView(size_hint = (1, 1))
        self.scroll.add_widget(self.txt)
        self.txt.bind(size = self.resize)
        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.scroll)
        layout.add_widget(self.inp)
        layout.add_widget(btn)
        
        self.add_widget(layout)
    def resize(self,width,heid):
        self.txt.text_size = (self.txt.width, None)
        self.txt.texture_update()
        self.txt.height = self.txt.texture_size[1]

    def next(self):
        global x1
        x1 =  self.inp.text
        self.manager.transition.direction = "left"
        self.manager.current = "second"
class SecondScr(Screen):
    def __init__(self, name = 'second'):
        super().__init__(name = name)
        self.txt = Label(text = 'Выполните 30 приседаний за 45 секунд', size_hint_y = None, font_size = '24sp')
        btn = ScrButton(self, "left", "third", text = "Продолжить", size_hint_y = None, font_size = '24sp')
        self.scroll =ScrollView(size_hint = (1, 1))
        self.scroll.add_widget(self.txt)
        self.txt.bind(size = self.resize)
        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.scroll)
        layout.add_widget(btn)
        self.add_widget(layout)
    def resize(self,width,heid):
        self.txt.text_size = (self.txt.width, None)
        self.txt.texture_update()
        self.txt.height = self.txt.texture_size[1]
class ThirdScr(Screen):
    def __init__(self, name = 'third'):
        super().__init__(name = name)
        self.txt = Label(text = 'В течение минуты замерьте пульс два раза: \n за первые 15 секунд минуты, затем за последние 15 секунд. \n Результаты запишите в соответствующие поля. ', size_hint_y = None, font_size = '24sp')
        btn = Button(text = "Завершить", size_hint_y = None, font_size = '24sp')
        self.inp1 = TextInput(multiline = False, text = 'Результат:', size_hint_y = None, font_size = '24sp')
        self.inp2 = TextInput(multiline = False, text = 'Результат после отдыха:', size_hint_y = None, font_size = '24sp')
        btn.on_press = self.next
        self.scroll =ScrollView(size_hint = (1, 1))
        self.scroll.add_widget(self.txt)
        self.txt.bind(size = self.resize)
        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.scroll)
        layout.add_widget(self.inp1)
        layout.add_widget(self.inp2)
        layout.add_widget(btn)
        self.add_widget(layout)
    def resize(self,width,heid):
        self.txt.text_size = (self.txt.width, None)
        self.txt.texture_update()
        self.txt.height = self.txt.texture_size[1]
    
    def next(self):
        global x2, x3
        x2 = self.inp1.text
        x3 = self.inp2.text
        self.manager.transition.direction = "left"
        self.manager.current = "fourth"
class FourthScr(Screen):
    def __init__(self, name = 'fourth'):
        super().__init__(name = name)
        self.txt = Label(text = ' ',  size_hint_y = None, font_size = '24sp')
        btn = ScrButton(self, "right", "main", text = "Хотите попробовать снова?",  size_hint_y = None, font_size = '24sp')
        self.scroll =ScrollView(size_hint = (1, 1))
        self.scroll.add_widget(self.txt)
        self.txt.bind(size = self.resize)
        self.on_enter = self.before
        layout = BoxLayout(orientation = "vertical")
        layout.add_widget(self.scroll)
        
        layout.add_widget(btn)
        
        self.add_widget(layout)

    def resize(self,width,heid):
        self.txt.text_size = (self.txt.width, None)
        self.txt.texture_update()
        self.txt.height = self.txt.texture_size[1]
    
    def before(self):
        a=str(index_ryf(int(x1), int(x2), int(x3)))
        self.txt.text = name + "\n"+v +"\n"+ "Ваш результат:"+ str(index_ryf(int(x1), int(x2), int(x3)))+ "\n" + str(test_ryf(int(v), float(a)))
        self.txt.texture_update()

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main'))
        sm.add_widget(FirstScr(name = 'first'))
        sm.add_widget(SecondScr(name = 'second'))
        sm.add_widget(ThirdScr(name = 'third'))
        sm.add_widget(FourthScr(name = 'fourth'))
        return sm
class pril(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        b = BoxLayout(orientation = "vertical")
        self.l = l = Label(text = "введите рост и вес через запятую")
        self.l2 = l2 = Label(text ="xod")
        self.inp = inp = TextInput(multiline = False)
        #img = AsyncImage(source = "")
        #b.add_widget(img)
        b.add_widget(l)
        b.add_widget(l2)
        b.add_widget(inp)
        s.add_widget(b)
        f.add_widget(s)
        inp.bind(text = self.kkk)
        return f
    def kkk(self,*b):
        self.l2.text = self.inp.text

MyApp().run()
