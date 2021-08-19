import sys
from math import log2
from itertools import combinations

#input = sys.stdin.readline
# sys.stdin.readline()
# sys.stdout.write("\n")

# # For getting input from input.txt file
# sys.stdin = open('Python_input1.txt', 'r')

# # Printing the Output to output.txt file
# sys.stdout = open('Python_output1.txt', 'w')


for _ in range(int(sys.stdin.readline())):
    n = str(sys.stdin.readline())
    n = n[:-1]
    # print(n)
    temp = 0
    # print(n[0])
    for i in range(len(n)):
        # print(n[i])
        if int(n[i]) % 2 == 0:
            temp = 1
    if temp:
        print(1)
    else:
        print(0)
