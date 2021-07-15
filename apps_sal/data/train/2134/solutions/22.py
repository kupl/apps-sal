def solve():
    a = [None] * (n + 1)

    a[1] = s[0]
    for i in range(2, n + 1):
        if s[i - 1] == -1:
            continue

        pi = p[i - 2]
        pi_er_pi = p[pi - 2]

        if s[i - 1] < s[pi_er_pi - 1]:
            return -1

        new_value = s[i - 1] - s[pi_er_pi - 1]
        a[pi] = min(a[pi] if a[pi] is not None else float('inf'), new_value)

    for i in range(2, n + 1):
        if s[i - 1] == -1:
            continue

        pi = p[i - 2]
        pi_er_pi = p[pi - 2]

        a[i] = s[i - 1] - s[pi_er_pi - 1] - a[pi]

    return sum(filter(None, a))


n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))
ans = solve()
print(ans)
