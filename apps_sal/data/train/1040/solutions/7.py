def compute_rich_substr(s):
    rich = [0 for _ in range(len(s) + 1)]

    for i in range(len(s) - 2):
        if (s[i] == s[i + 1]) or (s[i] == s[i + 2]) or (s[i + 1] == s[i + 2]):
            rich[i + 1] = rich[i] + 1
        else:
            rich[i + 1] = rich[i]

    rich[len(s) - 1] = rich[len(s)] = rich[len(s) - 2]
    return rich


t = int(input())

for _ in range(t):
    n, q = list(map(int, input().strip().split()))
    s = input()

    rich = compute_rich_substr(s)

    for _ in range(q):
        l, r = list(map(int, input().strip().split()))

        if r - l + 1 < 3:
            print("NO")
        elif rich[r - 2] - rich[l - 1] > 0:
            print("YES")
        else:
            print("NO")
