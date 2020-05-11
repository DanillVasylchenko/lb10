"""
    Реалізувати програмно мовою Python завдання з наведеного нижче списку. Для
кожної з задач алгоритм реалізувати з використанням рекурсії і ітерації. Аргументувати
письмово доцільність вибору в кожному випадку рекурсії або ітерації (використовувати
в якості критеріїв - час розробки та виконання програм, обсяг займаної пам'яті,
читабельність програми).

3. Сформувати функцію для переведення натурального числа з десяткової системи
числення у шістнадцятирічну.

Васильченко Даниїл 122 А
"""
from time import time


# РЕКУРСІЯ
def recursion_transfer_to_sixteen(number, sys=16):
    if not hasattr(recursion_transfer_to_sixteen, 'table'):
        recursion_transfer_to_sixteen.table = '0123456789ABCDEF'
    x, y = divmod(number, sys)
    return recursion_transfer_to_sixteen(x, sys) + recursion_transfer_to_sixteen.table[y] if x else \
        recursion_transfer_to_sixteen.table[y]


# ІТЕРАЦІЯ
def iteration_transfer_to_sixteen(number, sys=16):
    iteration_transfer_to_sixteen.table = '0123456789ABCDEF'
    r = ''
    while number:
        number, y = divmod(number, sys)
        r = iteration_transfer_to_sixteen.table[y] + r
    return r


x = int(input("ВВедіть число: "))
tic1 = time()
print("Результат виконання рекурсією: \n", recursion_transfer_to_sixteen(x))
toc1 = time()
recursion_time = toc1 - tic1
tic2 = time()
print("Результат виконання ітерацією: \n", iteration_transfer_to_sixteen(x))
toc2 = time()
iteration_time = toc2 - tic2
print()
print("Час розробки: обидва способи прості у реалізації, але рекурсія потребує менше коду\n"
      f"Час виконання: ітерація = {iteration_time}\n"
      f"               рекурсія = {recursion_time}\nІтерація виконується швидше\n"
      "Обсяг пам'яті: рекурсія забирає більше пам'яті через зберігання значень у стеку\n"
      "Читабельність загалом однакова")
