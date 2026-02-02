from typing import List


def string_length(word: str) -> int:
    return len(word)


def unite_strings(firstWord: str, secondWord: str) -> str:
    return firstWord + secondWord


def square_num(num: int) -> int:
    return num * num


def nums_sum(num1: int, num2: int) -> int:
    return num1 + num2


def devide_sum(num1: int, num2: int) -> tuple:
    devide_result = num1 / num2
    result_string = str(devide_result)
    result = result_string.split('.')
    return (result[0], result[1])


def avarage(list: List) -> int:
    result = 0
    for num in list:
        result += num
    return result / len(list)


def сommon_units(list1, list2):
    return list(set(list1) & set(list2))


def map_keys(map: dict):
    return map.keys()


def unite_dicts(dict_first: dict, dict_second: dict) -> dict:
    return {**dict_first, **dict_second}


def sets_intersect(set_first: set, set_second: set) -> set:
    return set_first.union(set_second)


def is_subset(set_first, set_second) -> set:
    return set_first.issubset(set_second)


def check_even_odd(num: int):
    if num % 2 == 0:
        print("Парне")
    else:
        print("Непарне")


def filter_even(numbers: List) -> List:
    return [num for num in numbers if num % 2 == 0]


# ?? задати питання
def check(num): return "парне" if num % 2 == 0 else "не парне"

check = lambda num: "парне" if num % 2 == 0 else "не парне"
