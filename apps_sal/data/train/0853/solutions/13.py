import operator
for _ in range(int(input())):
    n = int(input())
    d = dict()
    for i in range(n):
        value = input()
        key = int(input())
        d[key] = value
    for v in sorted(d):
        print(d[v])
