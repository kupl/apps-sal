N = int(input())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if A == B:
    print(0)
else:
    print(sum(A) - min([b for a, b in zip(A, B) if a > b]))
