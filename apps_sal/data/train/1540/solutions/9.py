# cook your dish here
n = int(input())
for i in range(n):
    a = int(input())
    b = int(input())
    if b % a == 0:
        print('YES')
    else:
        print('NO')
