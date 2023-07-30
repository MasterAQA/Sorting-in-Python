from random import randint

import pytest

from conftest import time_of_function

S = 10000
a = []
for i in range(S):
    a.append(randint(1, 99))

@time_of_function
def bubble_sort():
    i = 0
    while i < S - 1:
        j = 0
        while j < S - 1 -i:
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
            j += 1
        i += 1


if __name__ == '__main__':
    bubble_sort()

