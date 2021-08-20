(a, b) = [int(i) for i in input().split()]
x = b * (b - 1) // 2
y = b * a * (a + 1) // 2 + a
print(x * y % (10 ** 9 + 7))
