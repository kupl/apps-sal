from bisect import bisect_left, bisect_right


def go():
    # n = int(input())
    # a = list(map(int, input().split()))
    s = input()
    prev = -1
    mx = 0
    for i, aa in enumerate(s):
        if aa == 'R':
            mx = max(mx, i - prev)
            prev = i
    return max(mx, len(s) - prev)


t = int(input())
for _ in range(t):
    print(go())
