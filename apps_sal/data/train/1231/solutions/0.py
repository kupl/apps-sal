from operator import add
from functools import reduce

choices = []

for x in range(1800):
    num_str = list(map(int, str(2**x)))
    suma = reduce(add, num_str)
    choices.append(suma)
N = int(input())

for x in range(N):
    t = int(input())
    print(choices[t])
