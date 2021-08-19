t = int(input())
for _ in range(t):
    n = int(input())
    aa = list(map(int, input().split()))
    bb = list(map(int, input().split()))
    if aa[0] != 0 or bb[-1] != 0:
        print('No')
        continue
    if aa[-1] != bb[0]:
        print('No')
        continue
    if 0 in aa[1:] or 0 in bb[:n - 1]:
        print('No')
        continue
    ma = aa[-1]
    ans = 'Yes'
    for i in range(1, n - 1):
        if aa[i] + bb[i] < ma:
            ans = 'No'
        if aa[-1] + bb[i] < aa[i]:
            ans = 'No'
        if aa[i] + bb[0] < bb[i]:
            ans = 'No'
    print(ans)
