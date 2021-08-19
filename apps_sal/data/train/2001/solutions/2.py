(x, d) = map(int, input().split())
A = []
a = 1
k = 0
while a < x:
    a *= 2
a //= 2
x = bin(x)[2:][::-1]
y = 1
for i in range(len(x) - 1, -1, -1):
    if x[i] == '1':
        A += i * [y]
        k += 1
    y += d + 1
while k:
    A.append(y)
    y += d + 1
    k -= 1
print(len(A))
for i in A:
    print(i, end=' ')
