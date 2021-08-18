def balancedContest(n, p, arr):
    cakewalk = 0
    hard = 0
    for i in range(len(arr)):
        if arr[i] >= int(p / 2):
            cakewalk += 1
        if arr[i] <= int(p / 10):
            hard += 1
    if cakewalk == 1 and hard == 2:
        print('yes')
    else:
        print('no')
    return


t = int(input())
for _ in range(t):
    n, p = map(int, input().split())
    arr = list(map(int, input().split()))
    balancedContest(n, p, arr)
