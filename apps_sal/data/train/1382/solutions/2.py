# cook your dish here
n = int(input())
k = n + 1
total = 0
a = list(map(int, input().split()))
x = int(input())
a.sort(reverse=True)
for i in range(n):
    if a[i] < 0:
        k = i
        break
a = a[k:]
if a:
    n = len(a)
    if x > n:
        total -= sum(a)
    else:
        total -= sum(a[n - x:])
print(total)
