"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
"""

# put your python code here
sum = 0
while (1):
    i = int(input())
    if (i == 0):
        break
    sum += i
print(sum)
