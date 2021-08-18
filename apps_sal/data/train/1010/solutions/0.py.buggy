# code snippet reference:http://www.geeksforgeeks.org/searching-for-patterns-set    -2-kmp-algorithm/
def KMPMatch(pattern, string):
    M = len(pattern)
    N = len(string)
    nonlocal ans

    lps = [0] * M
    j = 0
    LPSCompute(pattern, M, lps)

    i = 0
    while i < N:
        if pattern[j] == string[i]:
            i += 1
            j += 1

        if j == M:
            ans += 1
            j = lps[j - 1]

        elif i < N and pattern[j] != string[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def LPSCompute(pattern, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]

            else:
                lps[i] = 0
                i += 1


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    s = list(map(int, input().split()))
    pattern = list(map(int, input().split()))
    ans = 0
    string = []
    for i in range(n - 1):
        string.append(s[i + 1] - s[i])
    KMPMatch(pattern, string)
    print(ans)
