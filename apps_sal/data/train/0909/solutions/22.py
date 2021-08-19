for _ in range(int(input())):
    N = int(input())
    barr = sorted(list(map(int, input().split())))
    garr = sorted(list(map(int, input().split())))
    tarr = barr + garr
    ans1 = [0] * (N * 2)
    ans2 = [0] * (N * 2)
    tarr.sort()
    j = 0
    for i in range(N):
        ans1[j] += garr[i]
        ans1[j + 1] += barr[i]
        ans2[j] += barr[i]
        ans2[j + 1] += garr[i]
        j += 2
    if ans1 == tarr or ans2 == tarr:
        print('YES')
    else:
        print('NO')
