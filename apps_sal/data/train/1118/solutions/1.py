def a(s, length):
    ans = 0
    for i in range(0, length):
        if i % 2 == 0 and s[i] == '1':
            ans += 1
        if i % 2 == 1 and s[i] == '0':
            ans += 1
    return min(ans, length - ans)


def b(s, length):
    ans = 0
    for i in range(0, length):
        if i % 2 == 0 and s[i] == '0':
            ans += 1
        if i % 2 == 1 and s[i] == '1':
            ans += 1
    return min(ans, length - ans)


for i in range(0, int(input())):
    n = int(input())
    s = input()
    print(min(a(s, n), b(s, n)))
