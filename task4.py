"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


syllable = 1
series_sum = 1


def get_series_sum(n):
    global syllable
    global series_sum
    syllable = syllable / -2
    series_sum += syllable
    n -= 1
    if n == 1:
        print(series_sum)
        return
    else:
        get_series_sum(n)


get_series_sum(5)
