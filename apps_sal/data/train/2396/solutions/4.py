def getAns(c, lo, hi, prefixCnt):
    if lo + 1 == hi:
        return 1 - (prefixCnt[c][hi] - prefixCnt[c][lo])
    mid = (lo + hi) // 2
    ans = 1 << 30
    ans = min(ans, (hi - lo) // 2 - (prefixCnt[c][mid] - prefixCnt[c][lo]) + getAns(c + 1, mid, hi, prefixCnt))
    ans = min(ans, (hi - lo) // 2 - (prefixCnt[c][hi] - prefixCnt[c][mid]) + getAns(c + 1, lo, mid, prefixCnt))
    return ans


for _ in range(int(input())):
    n = int(input())
    s = input()
    prefixCnt = [[0 for _ in range(n + 1)] for _ in range(26)]
    for i in range(n):
        for j in range(26):
            prefixCnt[j][i + 1] = prefixCnt[j][i]
        index = ord(s[i]) - ord('a')
        prefixCnt[index][i + 1] += 1
    print(getAns(0, 0, n, prefixCnt))
