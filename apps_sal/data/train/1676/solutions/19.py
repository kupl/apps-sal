import sys
(a, b, c) = list(map(int, input().split()))
rr = [0, 0, 5, 5]
cc = [0, 5, 0, 5]
cur = 0
while a != -1:
    ans = ''
    for i in range(3):
        if cur < 4:
            ans += str(i + 1) + ' ' + str(rr[cur] + 5) + ' ' + str(cc[cur] + 1) + ' '
        else:
            ans += '-1' + ' -1' + ' -1' + ' '
        cur += 1
    print(ans)
    sys.stdout.flush()
    (a, b, c) = list(map(int, input().split()))
