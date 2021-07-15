t = int(input())

for _ in range(t):
    n = int(input())
    l = [int(x) for x in input().split()]
    vals = [(x + i) % n for i, x in enumerate(l)]
    print("YES" if len(set(vals)) == n else "NO")

