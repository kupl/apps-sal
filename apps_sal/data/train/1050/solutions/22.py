def solve(S):
    ans = 0
    t = 0
    l = []

    for a in S:
        t += 1
        if a == '<':
            l.append(a)
        if a == '>':
            if len(l) == 0:
                return ans

            if len(l) > 0:
                l.pop()
                if len(l) == 0:
                    ans = t

    return ans


T = int(input())
ls = list()

for i in range(T):
    print(solve(input()))
