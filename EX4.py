# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

size = int(input ("Введите число N: "))
numbers_list = list(range(-size, size+1))
path = 'file.txt'
data = open(path, 'r')
mult = 1
for position in data:
    mult = numbers_list[int(position)] * mult
data.close()

print (f"Для N = {size}: {numbers_list}. Сумма = {mult}")