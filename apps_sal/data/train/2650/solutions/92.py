N, L = map(int, input().split())
w = []
for _ in range(N):
    w.append(input())

w.sort()

print("".join(w))
