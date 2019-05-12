"""
Напишите программу, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
"""

# put your python code here
inp = [i for i in input().split()]
inp.sort()
res = ''
j = 0
i = 0
while (i < len(inp)-1):
    if (inp[i] == inp[i + 1]):
        res = res + inp[i] + " "
        j = int(inp[i])
        if (i >= len(inp)-1):
            break
    i = i+1
    if (inp[i] == str(j)):
        while (inp[i] == str(j)):
            if (i >= len(inp)-1):
              break
            i = i+1
print(res)
