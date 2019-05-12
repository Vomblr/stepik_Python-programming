"""
Напишите программу, на вход которой подается одна строка с целыми числами. Программа должна вывести сумму этих чисел.

Используйте метод split строки.
"""

# put your python code here
inp = [int(i) for i in input().split()]
sum = 0
for i in range(len(inp)):
    sum = sum + inp[i]
print(sum)
