def main():
    import sys
    input = sys.stdin.readline
    S = input().rstrip('\n')
    N = len(S)
    rank = [0] * N
    seen = [0] * 26
    cnt = 0
    r = 0
    for i in range(N - 1, -1, -1):
        j = ord(S[i]) - 97
        if not seen[j]:
            seen[j] = 1
            cnt += 1
        rank[i] = r
        if cnt == 26:
            r += 1
            seen = [0] * 26
            cnt = 0
    ans = []
    for i in range(26):
        if not seen[i]:
            ans.append(i + 97)
            break
    i0 = 0
    while ord(S[i0]) != ans[0]:
        i0 += 1
        if i0 == N:
            print(chr(ans[0]))
            return
    r = rank[i0]
    seen2 = [0] * 26
    flg = 1
    for i in range(i0 + 1, N):
        j = ord(S[i]) - 97
        if flg:
            if rank[i] == r:
                seen2[j] = 1
            else:
                for k in range(26):
                    if not seen2[k]:
                        ans.append(k + 97)
                        break
                flg = 0
                seen2 = [0] * 26
                if j == k:
                    r -= 1
                    flg = 1
        elif j != k:
            continue
        else:
            r -= 1
            flg = 1
    for k in range(26):
        if not seen2[k]:
            ans.append(k + 97)
            break
    print(''.join(map(chr, ans)))


def __starting_point():
    main()


__starting_point()
