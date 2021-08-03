import sys
from math import log2
from itertools import combinations

#input = sys.stdin.readline
# sys.stdin.readline()
# sys.stdout.write("\n")

# For getting input from input.txt file
# sys.stdin = open('Python_input1.txt', 'r')

# # Printing the Output to output.txt file
# sys.stdout = open('Python_output1.txt', 'w')


for _ in range(int(sys.stdin.readline())):
    n, m = list(map(int, sys.stdin.readline().split()))
    a = set(map(int, sys.stdin.readline().split()))
    b = set(map(int, sys.stdin.readline().split()))
    c = []
    for i in a:
        if i not in b:
            c.append(i)
    for i in b:
        if i not in a:
            c.append(i)
    c = list(set(c))
    c.sort()
    print(*c)
