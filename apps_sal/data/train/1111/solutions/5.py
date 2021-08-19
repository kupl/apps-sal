# cook your dish here
from collections import Counter
for _ in range(int(input())):

    n = int(input())
    c = Counter([int(x) % 2 for x in input().split()])

    print(c[0] * c[1])
