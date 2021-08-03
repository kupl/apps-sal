# cook your dish here
t = int(input())
for k in range(t):
    n = int(input())
    lst = []
    for i in range(n):
        s, p, v = map(int, input().split())

        lst.append((p // (s + 1)) * v)
    print(max(lst))
