import sys
input = sys.stdin.readline
T, = list(map(int, input().split()))
for _ in range(T):
    a, b, c, d = list(map(int, input().split()))
    if a * c != b * d:
        print("NO")
        continue
    print("YES")
    R = [[0] * b for _ in range(a)]
    for v in range(a):
        v *= c
        s = [0] * b
        for i in range(c):
            s[(v + i) % b] = 1
        print("".join(str(x) for x in s))
