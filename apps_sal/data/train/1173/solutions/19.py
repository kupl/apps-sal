from collections import defaultdict


def solve(C, N):
    ar = [(0, -1)]
    cnt = defaultdict(list)
    cnt[0].append(-1)
    r = 0
    for i in range(len(C)):
        r = r ^ C[i]
        cnt[r].append(i)
    res = 0
    for l in cnt:
        for k in range(len(cnt[l]) - 1):
            for j in range(k + 1, len(cnt[l])):
                res += abs(cnt[l][k] - cnt[l][j]) - 1
    return res


def main():
    for _ in range(int(input())):
        N = int(input())
        C = list(map(int, input().split()))
        print(solve(C, N))


main()
