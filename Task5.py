# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.


ax = float(input('Задайте координаты для точки A по оси x:'))
ay = float(input('Задайте координаты для точки A по оси y:'))
bx = float(input('Задайте координаты для точки B по оси x:'))
by = float(input('Задайте координаты для точки B по оси y:'))

import math
distans = math.sqrt((ax-bx)**2+(ay-by)**2)
print(f'Растояние между точкой A до точки B = {distans}' )