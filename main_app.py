from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
from kivy.core.window import Window

from sits import Sits
from runner import Runner

colr = (0.1, 0.5, 0.3, 1)
Window.clearcolor = colr

btn_colr = (0.8, 1, 0.8, 1)

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False


age = 7
name = ''
p1, p2, p3 = 0, 0, 0



class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        instr = Label(text = txt_instruction)
        txt = '[i][color=6EEB5E]' + 'Введите имя:' + '[/color][/i]'   
        hl_0 = Label(text=txt, markup=True)     
        vl.add_widget(instr)


        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        in_name1 = Label(text = 'Введите имя:', halign='right')
        self.input = TextInput(multiline=False)
        hl_1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        in_age1 = Label(text = 'Введите возраст:', halign='right')
        self.input1 = TextInput(multiline=False)

        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_colr

        hl_0.add_widget(in_name1)
        vl.add_widget(hl_0)
        hl_0.add_widget(self.input)
        hl_1.add_widget(in_age1)
        vl.add_widget(hl_1)
        hl_1.add_widget(self.input1)

        vl.add_widget(self.btn)
        vl.add_widget(hl)
        self.add_widget(vl)

    def next(self):
        name = self.input.text
        age = check_int(self.input1.text)
        if age == False or age < 7:
            age = 7
            self.input1.text = str(age)
        else:
           self.manager.current = 'first'


     
class FirstScr(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False
        self.stage = 0
        super().__init__(**kwargs)
        self.hl_sec = Seconds(15)
        self.hl_sec.bind(done = self.sec_finished)
        self.hl = Label(text = 'Считайте пульс')

        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        test1 = Label(text = txt_test1)     
        vl.add_widget(test1)

        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        passw = Label(text = 'Введите результат', halign='right')
        self.input = TextInput(multiline=False)

        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        self.btn = Button(text='Закончить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_colr

        hl_0.add_widget(passw)
        vl.add_widget(hl_0)
        hl_0.add_widget(self.input)

        vl.add_widget(self.hl_sec)
        vl.add_widget(self.btn)
        vl.add_widget(hl)
        self.add_widget(vl)

    def sec_finished (self, *args):
        self.next_screen = True
        self.input.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.hl_sec.start()
        else:
            global p1
            p1 = check_int(self.input.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.input.text = str(p1)
            else:
                self.manager.current = 'second'




class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        instr = Label(text = txt_sits, size_hint=(0.5, 1))     

        self.lbl_sits = Sits(30)
        self.run = Runner(total=30, steptime=1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        line = BoxLayout()
        vlone = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        vlone.add_widget(self.lbl_sits)
        line.add_widget(instr)
        line.add_widget(vlone)
        line.add_widget(self.run)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = btn_colr
        self.btn.on_press = self.next

        vll = BoxLayout(orientation='vertical', padding=8, spacing=8)
        vll.add_widget(line)
        vll.add_widget(self.btn)
        self.add_widget(vll)

    def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'third'



class ThirdScr(Screen):
    def __init__(self, **kwargs):
        self.next_screen = False
        self.stage = 0
        super().__init__(**kwargs)
        self.hl_sec = Seconds(15)
        self.hl_sec.bind(done=self.sec_finished)
        self.hl = Label(text = 'Считайте пульс')

        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        sits = Label(text = txt_test3)     
        vl.add_widget(sits)


        hl_0 = BoxLayout(size_hint=(0.8, None), height='30sp')
        passw = Label(text = 'Результат:', halign='right')
        self.input = TextInput(multiline=False)
        hl_1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        passw1 = Label(text = 'Результат после отдыха:', halign='right')
        self.input1 = TextInput(multiline=False)

        hl = BoxLayout(size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5})
        self.btn = Button(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = btn_colr

        self.input.set_disabled(True)
        self.input1.set_disabled(True)


        vl.add_widget(self.hl)
        vl.add_widget(self.hl_sec)

        hl_0.add_widget(passw)
        vl.add_widget(hl_0)
        hl_0.add_widget(self.input)
        hl_1.add_widget(passw1)
        vl.add_widget(hl_1)
        hl_1.add_widget(self.input1)

        vl.add_widget(self.btn)
        vl.add_widget(hl)
        self.add_widget(vl)

    def sec_finished(self, *args):
        if self.hl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.hl_text = 'Отдыхайте'
                self.hl_sec.restart(30)
                self.input.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.hl_text =  'Считайте пульс'
                self.hl_sec.restart(15)
            elif self.stage == 2:
                self.input1.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn = 'Завершить'
                self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.hl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.input.text)
            p3 = check_int(self.input1.text)
            if p2 == False:
                p2 = 0
                self.input.text = str(p2)
            if p3 == False:
                p3 = 0
                self.input1.text = str(p3)
            else:
                self.manager.current = 'fourth'



class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.vl = BoxLayout(orientation = 'vertical')
        self.instr = Label(text = '')
        self.vl.add_widget(self.instr)
        self.add_widget(self.vl)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)
        # final_str = txt_index + ruffr_index + '/n' + txt-res[ruffier_result]



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm


app = MyApp()
app.run()

