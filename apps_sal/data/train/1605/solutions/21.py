(a, b) = input().split(' ')
a = int(a)
b = int(b)
result = a * b * (b - 1) * (a * b + b + 2) // 4
result = result % (10 ** 9 + 7)
print(result)
