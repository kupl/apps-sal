from sys import stdin
from math import *
line = stdin.readline().rstrip().split()
n = int(line[0])
numbers = stdin.readline().rstrip().split()[0]
numbers2 = stdin.readline().rstrip().split()[0]
cant00 = 0
cant01 = 0
cant11 = 0
cant10 = 0
for i in range(len(numbers)):
    if numbers[i] == '0' and numbers2[i] == '0':
        cant00 += 1
    if numbers[i] == '1' and numbers2[i] == '0':
        cant01 += 1
    if numbers[i] == '0' and numbers2[i] == '1':
        cant10 += 1
    if numbers[i] == '1' and numbers2[i] == '1':
        cant11 += 1
print(cant00 * cant01 + cant00 * cant11 + cant01 * cant10)
