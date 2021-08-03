l = input().split()
print(*l)
n = int(input())
for i in range(n):
    t = input().split()
    i = 0
    if l[1] == t[0]:
        i = 1
    l[i] = t[1]
    print(*l)
