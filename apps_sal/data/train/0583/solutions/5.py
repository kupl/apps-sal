n = int(input())
for i in range(n):
    a = int(input())
    l = [int(x) for x in input().split()]
    if sum(l) >= 0:
        print('YES')
    else:
        print('NO')
