import itertools
from typing import List, Dict
from itertools import product

N = int(input())
letter_order: Dict[str, int] = {}


def bubble_sort_count_swaps(arr):
    n = len(arr)
    swaps = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if letter_order[arr[j]] > letter_order[arr[j + 1]]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return swaps


for i in range(N):
    letter, number = input().split()
    letter_order[letter] = int(number)

# Ввод строки для сортировки
input_string = input()
input_list = list(input_string)

# Вызов функции для подсчета перестановок
swaps = bubble_sort_count_swaps(input_list)
print(swaps)
"""
<< INPUT >> 
3 
A 3
B 2
Z 1
ABZ
<< OUTPUT >> 
3
==================
<< INPUT >> 
5
A 10
C 5
D 7
X 4
Y 1
ACDAX
<< OUTPUT >> 
6
==================
"""
