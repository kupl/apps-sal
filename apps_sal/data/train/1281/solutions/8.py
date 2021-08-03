for i in range(int(input())):
    r = [1, 2, 3, 4, 5, 6, 7]
    N = int(input())
    li = list(map(int, input().split()))
    x = []

    for j in li:
        if j not in x:
            x.append(j)

    if li == li[::-1] and x == r:
        print('yes')
    else:
        print('no')
