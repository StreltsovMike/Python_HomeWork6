# Дз 2 задание 3
# Задайте список из k чисел последовательности 
# (1 + 1\k)^k и выведите на экран их сумму.
import math
from functools import reduce

k = int(input('Введите K : '))
nums = [(math.floor(((1 + 1/i)**i)*100)/100) for i in range(1, k+1)]
sum = reduce(lambda x,y: x + y, nums)
print(f'Сумма всех члеов списка {nums} = {sum}')