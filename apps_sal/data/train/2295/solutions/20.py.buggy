ans = 0
N = int(input())
A, B = zip(*list(list(map(int, input().split())) for _ in range(N)))
if A == B:
    print(0)
    return

Asum = sum(A)
ans = max(Asum - b for a, b in zip(A, B) if a > b)
print(ans)
