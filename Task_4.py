# дз 3 задание 2
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


n_list = [1, 2, 3, 4, 5, 6, 7, 8]

multi_list = [(n_list[i] * n_list[len(n_list) - 1 -i]) for i in range (len(n_list)-(len(n_list)//2))]

print(multi_list)