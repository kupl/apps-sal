
T = int(input())


def solve(n):
    li = list(map(int, list(str(n))))
    prev = 0
    f = {}
    for ind, it in enumerate(li):
        if it < prev:
            ind = f[prev]
            li[ind] -= 1
            for j in range(ind + 1, len(li)):
                li[j] = 9
            break
        prev = it
        if it not in f:
            f[it] = ind

    ans = 0
    for it in li:
        ans = 10 * ans + it

    return ans


for case in range(T):
    n = int(input())
    ans = solve(n)
    print(ans)
