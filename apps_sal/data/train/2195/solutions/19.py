from collections import Counter as co
x = int(input())
y = list(map(int, input().split()))
print(x - max(co(y).values()))
