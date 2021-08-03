from math import ceil
a = int(input())
*b, = map(int, input().split())
print(max(ceil(sum(b) / (a - 1)), max(b)))
