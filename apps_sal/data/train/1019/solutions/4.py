for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    if n % 2 == 0:
        print('no')
    elif l[0] != 1 or l[-1] != 1:
        print('no')
    else:
        l1 = list(range(1, n // 2 + 2))
        l2 = list(range(n // 2, 0, -1))
        if l[0:n // 2 + 1] == l1 and l[n // 2 + 1:] == l2:
            print('yes')
        else:
            print('no')
