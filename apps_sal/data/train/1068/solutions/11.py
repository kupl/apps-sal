# cook your dish here
x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    if((a * b) % 2 == 0):
        print('YES')
    else:
        print('NO')
