# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 19:36:48 2019

@author: Z
"""

import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

aa = datetime.datetime(2018,8,15,8,11,00)
bb = datetime.datetime.now()
cc = bb - aa
dd = str(cc)
days_ = int(dd.split()[0])
hours_ = int(dd.split()[2].split(':')[0])
mins_ = int(dd.split()[2].split(':')[1])
secs_ = int(dd.split()[2].split(':')[2].split('.')[0])

days = int(days_)
hours = int(dd.split()[0])*24 + int(hours_)
mins = hours*60 + int(mins_)
secs = mins*60 + int(secs_)

dDays = {1:'день',2:'дня',3:'дня',4:'дня',5:'дней',6:'дней',7:'дней',8:'дней',9:'дней',0:'дней'}
dHours = {1:'час',2:'часа',3:'часа',4:'часа',5:'часов',6:'часов',7:'часов',8:'часов',9:'часов',0:'часов'}
dMins = {1:'минута',2:'минуты',3:'минуты',4:'минуты',5:'минут',6:'минут',7:'минут',8:'минут',9:'минут',0:'минут'}
dSecs = {1:'секунда',2:'секунды',3:'секунды',4:'секунды',5:'секунд',6:'секунд',7:'секунд',8:'секунд',9:'секунд',0:'секунда'}
dDays2 = {11:'дней',12:'дней',13:'дней',14:'дней'}
dHours2 = {11:'часов',12:'часов',13:'часов',14:'часов'}
dMins2 = {11:'минут',12:'минут',13:'минут',14:'минут'}
dSecs2 = {11:'секунд',12:'секунд',13:'секунд',14:'секунд'}
def Text(time, dic, dic2):    
    if time < 10:
        text = str(time) + " " + str(dic[int(str(time)[-1])])
    else:
        if str(time)[:2] == '11' or str(time)[:2] == '12' or str(time)[:2] == '13' or str(time)[:2] == '14':  
            text = str(time) + " " + str(dic2[int(str(time)[:2])])
        else:
            text = str(time) +" " + str(dic[int(str(time)[-1])])
    return text

class FoxxyApp(BoxLayout):
    def __init__(self, **kwargs):
        super(FoxxyApp, self).__init__(**kwargs)
        self.orientation="vertical"
        self.add_widget(Label(text='Души лисички и пацана из Москвы соеденились:'))
        self.add_widget(Label(text=str(aa), color=[1, 255, 0, 1]))
        self.add_widget(Label(text='С тех пор прошло уже...'))
        self.add_widget(Label(text=Text(days_, dDays, dDays2) + ' ' + Text(hours_, dHours, dHours2) +' ' + Text(mins_, dMins, dMins2) + ' и ' + Text(secs_, dSecs, dSecs2)))
        self.add_widget(Label(text='Мы вместе вот уже ' + Text(hours, dHours, dHours2)))
        self.add_widget(Label(text='Мы счастливы ' + Text(mins, dMins, dMins2)))
        self.add_widget(Label(text='И любим друг друга ' + Text(secs, dSecs, dSecs2)))
        self.add_widget(Label(text='...Вместе мы преодолеем бесконечность!'))
        self.add_widget(Label(text='Потому что бесконечность - не предел.'))

class FoxxxyApp(App):
    def build(self):
        return FoxxyApp()

if __name__ == '__main__':
   FoxxxyApp().run()
