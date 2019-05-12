"""Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы 𝐴 часов в сутки, но пересыпать тоже вредно и не стоит спать более 𝐵 часов. Сейчас Аня спит 𝐻 часов в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите “Это нормально”. Если Аня спит менее 𝐴 часов, выведите “Недосып”, если же более 𝐵 часов, то выведите “Пересып”.

Получаемое число 𝐴 всегда меньше либо равно 𝐵.

На вход программе в три строки подаются переменные в следующем порядке: 𝐴, 𝐵, 𝐻.

Обратите внимание на регистр символов: вывод должен в точности соответствовать описанному в задании, т. е. если программа должна вывести "Пересып", выводы программы "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.

Это первое не самое тривиальное задание на условное выражение. В случаях, когда разбить исполнение программы на несколько направлений, стоит внимательно обдумать все условия, которые нужно использовать. Особое внимание стоит уделить строгости используемых условных операторов: различайте < и ≤; > и ≥. Для того, чтобы понимать, какой из них стоит использовать, внимательно прочитайте условие задания."""

# put your python code here
A = int(input())
B = int(input())
H = int(input())

if (A<=H<=B):
    print('Это нормально')
elif H < A:
    print('Недосып')
else:
    print('Пересып')