for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    MAT = [0]
    cur = 0
    for i in range(n):
        a[i] = str(bin(a[i]))[-1]
        if a[i] == '0':
            cur += 1
        MAT.append(cur)
    for i in range(int(input())):
        (l, r) = map(int, input().split())
        if MAT[r] - MAT[l - 1] == 0:
            print('ODD')
        else:
            print('EVEN')
