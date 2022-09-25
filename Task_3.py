# дз 3 задание 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.

n_list = [1.1, 2.2, 3.1, 4.5001, 6.01]
ostatok_list = list(map(lambda x: round((x % 1), 5), n_list))
max, min = 0, 1
for i in range(len(ostatok_list)):
    if(ostatok_list[i] > max):
        max = ostatok_list[i]
    elif(ostatok_list[i] < min):
        min = ostatok_list[i]
print(f'{max} - {min} = {max-min}')
