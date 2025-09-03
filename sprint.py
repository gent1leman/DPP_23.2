import turtle
import random
import time

# Глобальные переменные
'''Использование глоальных переменных в функциях '''
sc = None
t1 = None
t2 = None
win = False

# Функция базовой настройки 
'''Логика настроек программы'''
def setup():
    global sc, t1, t2
    sc = turtle.Screen()
    sc.setup(500,500)
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t1.color('red')
    t2.color('blue')
    t1.shape('turtle')
    t2.shape('turtle')
    t1.penup()
    t1.penup()
    t1.goto(-150,50)
    t2.goto(-150,-50)
    
# Функция запуска игры
''' отсутствие структуры (веь алгоритм написан на функциях, а не на классах)'''
def start_race():
    global win 
    for i in range(100):
        if not win:
            t1.forward(random.randint)
            t1.forward(random.randint)
            check_winner()
        else:
            break

# Функция для определения победителя
'''отсутствие структуры (веь алгоритм написан на функциях, а не на классах)'''
def check_winner():
    global win
    if t1.xcor() > 150:
        print('победила красная черепашка')
        win = True
    if t1.xcor() > 150:
        print('победила синяя черепашка')
        win = True
        
# Код запуска
'''Логика игрового процесса'''
setup()
start_race()
        
''' Код невозможно переиспользовать, поскольку он не представляет собой модуль'''
