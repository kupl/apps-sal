from collections import *
for _ in range(int(input())):
    n = int(input())
    l = [*map(int, input().split())]
    ans = 0
    ind = defaultdict(list)
    even = []
    odd = []
    for i in range(n):
        ind[l[i]].append(i)
        if l[i] % 2 == 0:
            if not even:
                even.append(1)
            else:
                even.append(even[-1] + 1)
        elif not even:
            even.append(0)
        else:
            even.append(even[-1])
        if l[i] % 2 == 1:
            if not odd:
                odd.append(1)
            else:
                odd.append(odd[-1] + 1)
        elif not odd:
            odd.append(0)
        else:
            odd.append(odd[-1])
    pre_sum = [l[0]]
    for i in range(1, n):
        pre_sum.append(pre_sum[-1] + l[i])
    for i in ind:
        x = len(ind[i])
        if x > 1:
            for j in range(x - 1):
                if i % 2 == 0:
                    if ind[i][j] > 0 and even[ind[i][j] + 1] != even[ind[i][j]] and ((even[ind[i][j + 1] - 1] - even[ind[i][j] + 1] + 1) % 2 == 0):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] == 0 and even[ind[i][j] + 1] != even[ind[i][j]] and ((even[ind[i][j + 1] - 1] - even[ind[i][j] + 1] + 1) % 2 == 0):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] == 0 and even[ind[i][j] + 1] == even[ind[i][j]] and ((even[ind[i][j + 1] - 1] - even[ind[i][j] + 1]) % 2 == 0):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] > 0 and even[ind[i][j] + 1] == even[ind[i][j]] and ((even[ind[i][j + 1] - 1] - even[ind[i][j] + 1]) % 2 == 0):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                if i % 2 == 1:
                    if ind[i][j] > 0 and odd[ind[i][j] + 1] != odd[ind[i][j]] and ((odd[ind[i][j + 1] - 1] - odd[ind[i][j] + 1] + 1) % 2 == 1):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] == 0 and odd[ind[i][j] + 1] == odd[ind[i][j]] and ((odd[ind[i][j + 1] - 1] - odd[ind[i][j] + 1]) % 2 == 1):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] == 0 and odd[ind[i][j] + 1] != odd[ind[i][j]] and ((odd[ind[i][j + 1] - 1] - odd[ind[i][j] + 1] + 1) % 2 == 1):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
                    elif ind[i][j] > 0 and odd[ind[i][j] + 1] == odd[ind[i][j]] and ((odd[ind[i][j + 1] - 1] - odd[ind[i][j] + 1]) % 2 == 1):
                        ans = max(ans, pre_sum[ind[i][j + 1] - 1] - pre_sum[ind[i][j]])
    print(ans)
