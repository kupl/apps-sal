def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    b = [v for v in a]
    b.append(0)
    b.sort()
    dic = {}
    cnt = []
    num = []
    for v in b:
        if v in dic:
            cnt[dic[v]] += 1
        else:
            p = len(cnt)
            cnt.append(1)
            dic[v] = p
            num.append(v)
    min_idx = [n] * len(cnt)
    for i, v in enumerate(a):
        if min_idx[dic[v]] > i:
            min_idx[dic[v]] = i
    for i in reversed(range(1, len(cnt))):
        dif = num[i] - num[i - 1]
        ans[min_idx[i]] += dif * cnt[i]
        if min_idx[i - 1] > min_idx[i]:
            min_idx[i - 1] = min_idx[i]
        cnt[i - 1] += cnt[i]
    for v in ans:
        print(v)


def __starting_point():
    main()


__starting_point()
