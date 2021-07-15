from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])

numbers = list(map(int, stdin.readline().rstrip().split()))

scoreSon = sum(numbers)

numBefore = 0

for i in range(n-1):
    numbers = list(map(int, stdin.readline().rstrip().split()))
    score = sum(numbers)
    if score > scoreSon:
        numBefore+=1
print(numBefore+1)


