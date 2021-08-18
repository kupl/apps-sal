N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

A, B = list(zip(*AB))

if A == B:
    print((0))
    return

ans = sum(A)

ans -= min([b for a, b in AB if b < a])
print(ans)
