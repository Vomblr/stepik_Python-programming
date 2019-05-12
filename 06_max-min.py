"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
"""

# put your python code here
a = int(input())
b = int(input())
c = int(input())

max = a
if max < b:
    max = b
if max < c:
    max = c
print(max)
min = a
if min > b:
    min = b
if min > c:
    min = c
print(min)
print((a + b + c) - (min + max))
