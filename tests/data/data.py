from random import randint

from conftest import data

S = data.count_number
a = []
for i in range(S):
    a.append(randint(1, 999))
