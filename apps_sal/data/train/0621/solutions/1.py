s = []


def chk(st, n):
    for x in s:
        if st not in x:
            return 0
    return 1


for t in range(eval(input())):
    n = eval(input())
    s = list(input().split())

    mx = -1
    ans = ""

    for i in range(len(s[0])):
        for j in range(i, len(s[0])):
            if chk(s[0][i:j + 1], n):
                if mx == j + 1 - i:
                    ans = min(ans, s[0][i:j + 1])
                if mx < j + 1 - i:
                    mx = j + 1 - i
                    ans = s[0][i:j + 1]

    print(ans)
