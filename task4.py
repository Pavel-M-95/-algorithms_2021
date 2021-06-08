"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    n = max(array, key=array.count)
    m = array.count(n)
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(func_1())
print(func_2())
print(func_3())

t1 = timeit("func_1()", globals=globals(), number=1000)
t2 = timeit("func_2()", globals=globals(), number=1000)
t3 = timeit("func_3()", globals=globals(), number=1000)
print(t1)
print(t2)
print(t3)


""" Замеры:
0.008998300000000008
0.0043073
0.0031542999999999988
Самая меделенная - это первая функциия, т.к. она осуществляет перебор всех чисел списка, вторая функцияя создает новые
списки, в связи с этим процесс обработки замедляется. Вариант 3 быстрее, т.к. максимальное число оперделяется 
изначально.
"""
