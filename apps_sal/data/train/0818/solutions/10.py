for i in range(int(input())):
    n = int(input())
    y = [int(x) for x in input().split()]
    y = [x % 2 for x in y]
    lst = [0]
    lst.extend(y)
    for j in range(n + 1):
        if lst[j] == 0:
            lst[j] = lst[j - 1] + 1
        else:
            lst[j] = lst[j - 1]
    for j in range(int(input())):
        (l, r) = map(int, input().split())
        if lst[r] - lst[l - 1] > 0:
            print('EVEN')
        else:
            print('ODD')
