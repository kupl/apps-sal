N = int(input())
a = []
b = []
for i in range(N):
    (tmp1, tmp2) = list(map(int, input().split()))
    a.append(tmp1)
    b.append(tmp2)
count = 0
ls_l = [i for i in range(N) if a[i] > b[i]]
ls_m = [i for i in range(N) if a[i] == b[i]]
ls_s = [i for i in range(N) if a[i] < b[i]]
flg = 1
if len(ls_l) > 1:
    ls_l2 = [(b[i], i) for i in ls_l]
    ls_l2.sort()
    idx = ls_l2[0][1]
    count = sum(a) - b[idx]
elif len(ls_m) == N:
    count = 0
else:
    for idx in ls_m:
        count += a[idx]
    for idx in ls_s:
        count += a[idx]
    if flg == 1:
        for idx in ls_l:
            count += a[idx] - b[idx]
print(count)
