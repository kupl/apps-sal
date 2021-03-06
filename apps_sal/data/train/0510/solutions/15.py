import bisect


def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    L = [[] for x in range(26)]
    for (idx, s) in enumerate(S):
        L[ord(s) - ord('a')].append(idx)
    for _ in range(Q):
        row = input().split()
        if row[0] == '1':
            (y, z) = (int(row[1]) - 1, row[2])
            if S[y] != z:
                idx_target = ord(S[y]) - ord('a')
                idx_del = bisect.bisect_left(L[idx_target], y)
                if idx_del < len(L[idx_target]):
                    L[idx_target].pop(idx_del)
                bisect.insort(L[ord(z) - ord('a')], y)
                S[y] = z
        elif row[0] == '2':
            (y, z) = (int(row[1]) - 1, int(row[2]) - 1)
            answer = 0
            for idx_alphabet in range(26):
                left = bisect.bisect_left(L[idx_alphabet], y)
                if left < len(L[idx_alphabet]) and y <= L[idx_alphabet][left] <= z:
                    answer += 1
            print(answer)
    pass


def __starting_point():
    main()


__starting_point()
