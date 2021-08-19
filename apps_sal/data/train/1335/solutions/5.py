# cook your dish here
n = int(input())
a = list(map(int, input().split()))
b = set(a)
c = 0
for j in b:
    x = a.count(j)
    c += (x // 2) + (x % 2)
print(c)
