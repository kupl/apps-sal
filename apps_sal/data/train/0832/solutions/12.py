from itertools import combinations
t = int(input())
for i in range(t):
    (n, k) = map(int, input().split())
    num = list(map(int, input().split(maxsplit=n)))
    y = list(combinations(num, k))
    num1 = []
    for i in range(len(y)):
        num1.append(sum(y[i]))
    print(num1.count(min(num1)))
