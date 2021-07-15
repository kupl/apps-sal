from math import sqrt

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    
    if a == 0 or b == 0 or c == 0:
        print('NO')
        continue
    
    x = a ** 2 + b ** 2 == c ** 2
    y = a ** 2 + c ** 2 == b ** 2
    z = b ** 2 + c ** 2 == a ** 2
    
    print('YES' if x or y or z else 'NO')
