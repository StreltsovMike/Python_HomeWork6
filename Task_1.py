# Дз 3, задание 1
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции
from random import randint
from functools import reduce

n = int(input('Введите N : '))
n_list = [randint((-n),(n)) for i in range(n)]
n2_list = [n_list[i] for i in range(1, n, 2)]
sum = reduce(lambda x,y: x + y, n2_list)
print(f'Сумма нечетных элементов списка {n_list} = {sum}')