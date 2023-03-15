#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
number = int(input("Введите длину массива: "))
n = int(input("Введите натуральное число: "))
index = 0
list = []
for i in range(1, number+1):
    i = random.randint(1, number)
    list.append(i)
print(list)
for j in range(len(list)):
    if n == list[j]:
        index += 1
print(f"Количество числа {n} в массиве - {index}")