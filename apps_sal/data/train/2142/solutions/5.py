n = int(input())
a = [0]*n
for i in range(n):
    for x in map(int, input().split()):
        if x!=-1:
            a[i]|=x
print(*a)

