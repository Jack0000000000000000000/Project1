from kivy.uix.label import Label
from kivy.clock import Clock


class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.total = total
        self.current =  0
        my_text = 'Осталость приседаний: ' + str(total)
        super().__init__(text = my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        remain = max(0, self.total - self.current)
        self.text = 'Осталость приседаний: ' + str(remain)
        # self.text = my_text




