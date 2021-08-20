x = int(input())


def minReplacement(s, length):
    ans = 0
    for i in range(0, length):
        if i % 2 == 0 and s[i] == '1':
            ans += 1
        if i % 2 == 1 and s[i] == '0':
            ans += 1
    return min(ans, length - ans)


for i in range(x):
    length = int(input())
    s = input()
    print(minReplacement(s, length))
