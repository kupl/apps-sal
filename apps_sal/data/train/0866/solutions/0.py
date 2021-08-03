t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if sum(l) != n or max(l) == n:
        print('-1')
    else:
        d = dict()
        ans = [-1] * n
        for i in range(0, n):
            d[i] = 1
        for i in range(n):
            if l[i] != 0:
                count = l[i]
                for k, v in list(d.items()):
                    if count > 0 and v == 1 and i != k:
                        d[k] = 0
                        ans[k] = i + 1
                        count -= 1
        ind = -1
        for i in range(0, len(ans)):
            if ans[i] == -1:
                ind = i
        if ind == -1:
            print(*ans)
        else:
            for i in range(len(ans)):
                if ans[i] != ind + 1:

                    ans[ind] = ans[i]
                    ans[i] = ind + 1
                    break
            print(*ans)
