"""
Когда Павел учился в школе, он запоминал таблицу умножения прямоугольными блоками. Для тренировок ему бы очень пригодилась программа, которая показывала бы блок таблицы умножения.

Напишите программу, на вход которой даются четыре числа 𝑎, 𝑏, 𝑐 и 𝑑, каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [𝑎;𝑏] на все числа отрезка [𝑐;𝑑].

Числа 𝑎, 𝑏, 𝑐 и 𝑑 являются натуральными и не превосходят 10, 𝑎≤𝑏, 𝑐≤𝑑.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте '\t' — символ табуляции. Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных отрезков — заголовочные столбец и строка таблицы.﻿
"""

# put your python code here
a, b, c, d = int(input()), int(input()), int(input()), int(input())
print(end = '\t')
for i in range(c, d + 1):
    print(i, end = '\t')
print("")
for i in range(a, b+1):
    print(i, end = '\t')
    for n in range(c, d + 1):
        print(i * n, end = "\t")
    print("")
