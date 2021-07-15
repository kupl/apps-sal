n = int(input())

if n % 2 == 0:
    print('NO')
    return

print('YES')

for i in range(n):
    print(2*i + i % 2 + 1, end=' ')
for i in range(n):
    print(2*i - i % 2 + 2, end=' ')
print()

