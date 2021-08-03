n = int(input())
arr = list(map(int, input().split()))
x = int(input())
l = []
for i in arr:
    if i < 0:
        l.append(i)
l.sort(reverse=True)
s = 0
inc = 0
z = len(l)
for i in range(len(l)):
    if x <= z:
        l[i] += inc
        s += abs(l[i]) * x
        inc += abs(l[i])
        z -= 1
    else:
        l[i] += inc
        s += abs(l[i])
print(s)
