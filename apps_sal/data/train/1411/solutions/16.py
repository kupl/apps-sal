import math
for _ in range(int(input())):
    (x, r, a, b) = list(map(int, input().split()))
    s1 = max(a, b)
    s2 = min(a, b)
    circum = 2 * math.pi * r
    total_dist = circum * x
    total_time = total_dist / s1
    first_interaction = circum / (s1 - s2)
    ans = int(total_time / first_interaction)
    if total_time != first_interaction:
        print(ans)
    else:
        print(max(ans - 1, 0))
