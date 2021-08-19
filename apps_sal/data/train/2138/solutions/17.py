A = list(input())
B = list(input())
zA = A.count('1')
zA += zA & 1
if zA >= B.count('1'):
    print('YES')
else:
    print('NO')
