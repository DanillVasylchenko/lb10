"""
    Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для
кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації. Аргументувати
письмово доцільність вибору в кожному випадку рекурсії або ітерації (використовувати
в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті,
читабельність програми).

3. Сформувати функцію для обчислення індексу максимального елемента масиву
n*n, де 1<=n<=5.

Васильченко Даниїл 122 А
"""
from time import time  # для підрахунку часу виконання треба використовувати великі значення
import numpy as np


# ІТЕРАЦІЯ
def iteration_max_num_index(arr, max_num=0):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if max_num < arr[i][j]:
                max_num = arr[i][j]
    return max_num


# РЕКУРСІЯ
def recursion_max_num_index(array, count=0, temp=0, i=0, j=0):
    if temp == len(array[count]):
        count += 1
        temp = 0
    if count == len(array):
        return i, j
    if array[count][temp] > array[i][j]:
        i = count
        j = temp
    temp += 1
    return recursion_max_num_index(array, count, temp, i, j)


while True:
    n = int(input("Введіть розмірність: "))
    if n in range(1, 6):
        break

x = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        x[i, j] = int(input("Введіть число: "))
print("Ваш масив: \n", x)

tic1 = time()
print("Результат виконання рекурсією: \n", recursion_max_num_index(x))
toc1 = time()
recursion_time = toc1 - tic1
tic2 = time()
print("Результат виконання ітерацією: \n", iteration_max_num_index(x))
toc2 = time()
iteration_time = toc2 - tic2
print()
print("Час розробки: обидва способи прості у реалізації, але ітерація потребує менше коду\n"
      f"Час виконання: ітерація = {iteration_time}\n"
      f"               рекурсія = {recursion_time}\nІтерація виконується швидше\n"
      "Обсяг пам'яті: рекурсія забирає більше пам'яті через зберігання значень у стеку та використанная більшої "
      "кількості змінних\n "
      "Ітерація читабельніша")
