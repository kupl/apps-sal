t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    lst = [int(x) for x in input().split()]
    for j in range(len(lst)):
        if lst[j] >= x:
            print('YES')
            break
    else:
        print('NO')
