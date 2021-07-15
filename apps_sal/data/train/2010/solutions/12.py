
n = int(input())
a = [int(x) for x in input().split()]

a[0] = 1
a[-1] = 1
for i in range(1,n):
    a[i] = min(a[i],a[i-1]+1)
    a[-i] = min(a[-i],a[-(i-1)]+1)

print(max(a))


