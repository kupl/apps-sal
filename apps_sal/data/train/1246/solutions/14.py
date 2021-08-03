t = int(input())
while(t > 0):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    if max(a) != max(b):
        print('YES')
    else:
        print('NO')
    t -= 1
