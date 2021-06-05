from time import time_ns


def timeit(func):
    def decoration(*args, **kwargs):
        start = time_ns()
        result = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__}: {time_ns() - start}')
        return result

    return decoration


@timeit
def dict_fill(test_dict: dict, n: int) -> dict:
    for i in range(1, n + 1):
        test_dict[i] = i
    return test_dict


@timeit
def list_fill(test_list: list, n: int) -> list:
    for i in range(1, n + 1):
        test_list.append(i)
    return test_list


@timeit
def dict_search(test_dict: dict, st: str) -> int:
    return test_dict.get(st, 0)


@timeit
def list_search(test_list: list, st: str) -> int:
    return test_list.index(st)


a = []
b = {}
test_ls = [str(i) for i in range(1000000)]
test_dict = {str(i): i for i in range(1000000)}

dict_fill({}, 100000)
list_fill([], 100000)
dict_search(test_dict, '999999')
list_search(test_ls, '999999')

"""
Время выполнения dict_fill: 16835100 - медленнее, чем у списка при одинаковой сложности O(n)
Время выполнения list_fill: 15720400
Время выполнения dict_search: 0 - моментально, сложность О(1)
Время выполнения list_search: 21959400 - сложность О(n)
"""