S = input()
N = len(S)
if (
    S[0] == "0" or
    S[-1] == "1" or
    any(S[i] != S[N - i - 2] for i in range((N - 1) // 2))
):
    print(-1)
    return

head = 0
edges = []
for i in range(N - 1):
    edges.append((head, i + 1))
    if S[i] == "1":
        head = i + 1
[print(f + 1, t + 1) for f, t in edges]
