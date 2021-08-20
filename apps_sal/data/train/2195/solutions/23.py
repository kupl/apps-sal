from collections import *
print(int(input()) - max(Counter(map(int, input().split())).values()))
