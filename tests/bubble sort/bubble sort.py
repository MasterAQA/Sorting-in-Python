from random import randint

from conftest import time_of_function



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

