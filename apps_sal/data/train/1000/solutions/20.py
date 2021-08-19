import math
for test in range(int(input())):
    length = int(input())
    smallest = min([int(x) for x in input().split()])
    print(math.ceil(length / smallest))
