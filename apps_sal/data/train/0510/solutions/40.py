import bisect
N = input()
S = list(input())
alphabet = [[] for _ in range(26)]
for i, s in enumerate(S):
    alphabet[ord(s) - ord('a')].append(i)
Q = int(input())
for _ in range(Q):
    Type, A, B = input().split()
    if Type == "1":
        A = int(A)
        s = S[A - 1]
        if s == B:
            continue
        o = ord(s) - ord("a")
        alphabet[o].pop(bisect.bisect_left(alphabet[o], A - 1))
        index = bisect.bisect(alphabet[ord(B) - ord("a")], A - 1)
        alphabet[ord(B) - ord("a")].insert(index, A - 1)
        S[A - 1] = B
    else:
        A = int(A)
        B = int(B)
        ans = 0
        for i in range(26):
            indexL = bisect.bisect_left(alphabet[i], A - 1)
            if indexL == len(alphabet[i]):
                continue
            ans += (alphabet[i][indexL] <= B - 1)
        print(ans)
