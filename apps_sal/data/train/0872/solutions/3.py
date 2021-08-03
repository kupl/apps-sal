for i in range(int(input())):
    z, a, b, k = list(map(int, input().split()))
    n = 0
    for j in range(1, z + 1):
        if j % a == 0 and j % b == 0:
            pass
        elif j % a == 0:
            n += 1
        elif j % b == 0:
            n += 1
    if n >= k:
        print('Win')
    else:
        print('Lose')
