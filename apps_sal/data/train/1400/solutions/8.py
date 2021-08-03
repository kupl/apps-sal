t = int(input())
for jkl in range(t):
    n, l, r = list(map(int, input().split(" ")))
    min_su = 0
    stoped = 0
    for i in range(0, l):
        min_su = min_su + (2 ** i)
        stoped = i
    max_su = min_su
    for i in range(l, r):
        max_su = max_su + (2 ** i)
        stoped = i
    for i in range(n - l):
        min_su = min_su + 1
    for i in range(n - r):
        max_su = max_su + (2 ** stoped)
    print(min_su, max_su)
