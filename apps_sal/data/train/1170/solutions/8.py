t = int(input())
for z in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in a:
        if i % k == 0:
            print('1', end='')
        else:
            print('0', end='')
    print()
