
import bisect

N = int(input())
S = input()
Q = int(input())

cS = [""] * N
char_idxs = [[]for _ in range(26)]

for i, s in enumerate(S):
    cS[i] = s
    char_idxs[ord(s) - 97].append(i)

query = [tuple(map(str, input().split())) for _ in range(Q)]


for q, a, b in query:

    if q == "1":
        if cS[int(a) - 1] == b:
            continue
        else:

            idx = bisect.bisect_right(char_idxs[ord(cS[int(a) - 1]) - 97], int(a) - 1)
            if char_idxs[ord(cS[int(a) - 1]) - 97][idx - 1] == int(a) - 1:
                char_idxs[ord(cS[int(a) - 1]) - 97][idx - 1:idx] = []

            bisect.insort_right(char_idxs[ord(b) - 97], int(a) - 1)

            cS[int(a) - 1] = b

    else:
        cnt = 0
        for i in range(26):
            if len(char_idxs[i]) == 0:
                continue
            l = bisect.bisect_left(char_idxs[i], int(a) - 1)

            if l < len(char_idxs[i]) and char_idxs[i][l] <= int(b) - 1:
                cnt += 1

        print(cnt)
