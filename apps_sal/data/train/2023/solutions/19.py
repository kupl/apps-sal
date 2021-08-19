from sys import stdin
from math import *

line = stdin.readline().rstrip().split()
n = int(line[0])
sizeG = int(floor(sqrt(n)))
cantG = int(ceil(n / sizeG))

for i in range(cantG - 1):
    for j in range(sizeG, 0, -1):
        print(j + i * sizeG, end=" ")
for j in range(n, (cantG - 1) * sizeG, -1):
    print(j, end=" ")

# for i in range(int(n/2)):
 #   print((i+1)*2, end=" ")
# for i in range(int(n/2)):
#    print((i+1)*2-1, end=" ")
# if n % 2==1:
#    print(n)
