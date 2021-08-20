T = int(input())
for i in range(T):
    (lower, upper) = (0, 0)
    (N, K) = list(map(int, input().split()))
    s = str(input())[:N]
    for j in range(len(s)):
        if s[j] >= 'a' and s[j] <= 'z':
            lower += 1
        elif s[j] >= 'A' and s[j] <= 'Z':
            upper += 1
    if lower <= K and upper <= K:
        print('both')
    elif lower <= K and upper >= K:
        print('brother')
    elif lower >= K and upper <= K:
        print('chef')
    elif lower >= K and upper >= K:
        print('none')
