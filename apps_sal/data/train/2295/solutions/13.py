N = int(input())
AB = [[int(i) for i in input().split()] for _ in range(N)]

s = 0
m = float('inf')
for i, (A, B) in enumerate(AB) :
    s += A
    if A > B :
        m = min(m, B)

if m == float('inf') :
    print(0)
else :
    print(s - m)
