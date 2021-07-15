N, L = map(int, input().split())
S = [""] * N
for i in range(N):
    S[i] = input()

S.sort()
for s in S:
    print(s, end = "")
