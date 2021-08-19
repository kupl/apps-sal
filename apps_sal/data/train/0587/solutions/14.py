# cook your dish here
n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    num = a[i]
    b.append(num)
    num //= 2
    if num % 2 == 1:
        b[i] -= 2
    else:
        b[i] += 2
    if b[i] == 0:
        b[i] = 1
print(*b)
