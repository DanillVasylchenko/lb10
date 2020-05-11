"""
    Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для
кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації. Аргументувати
письмово доцільність вибору в кожному випадку рекурсії або ітерації (використовувати
в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті,
читабельність програми).

2. Сформувати функцію, що визначатиме чи є задане натуральне число простим.
Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого
себе).

Васильченко Даниїл 122 А
"""
import math
from time import time


# РЕКУРСІЯ
def recursion_simple_num(number, d=2):
    if number < d:
        return False
    elif number == d:
        return True
    elif number % d == 0:
        return False
    else:
        return recursion_simple_num(number, d + 1)


# ІТЕРАЦІЯ
def iteration_simple_num(number):
    if number < 2:
        return False
    if number == 2:
        return True
    limit = math.sqrt(number)
    i = 2
    while i <= limit:
        if number % i == 0:
            return False
        i += 1
    return True


x = int(input("ВВедіть число: "))
tic1 = time()
print("Результат виконання рекурсією: \n", recursion_simple_num(x))
toc1 = time()
recursion_time = toc1 - tic1
tic2 = time()
print("Результат виконання ітерацією: \n", iteration_simple_num(x))
toc2 = time()
iteration_time = toc2 - tic2
print()
print("Час розробки: обидва способи прості у реалізації, але рекурсія потребує менше коду\n"
      f"Час виконання: ітерація = {iteration_time}\n"
      f"               рекурсія = {recursion_time}\nІтерація виконується швидше\n"
      "Обсяг пам'яті: рекурсія забирає більше пам'яті через зберігання значень у стеку\n"
      "Рекурсія читабельніша")
