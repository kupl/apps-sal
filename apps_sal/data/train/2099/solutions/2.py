def printList(a):
    print(" ".join(map(str, a)))


def solve():
    n, k = list(map(int, input().split()))
    if k == 1:
        printList(list(range(1, n + 1)))
        return

    cur = k + 1
    sh = k
    sg = -1
    ans = []
    while True:
        ans.append(cur)
        cur += sh * sg
        if not sh:
            break
        sh -= 1
        sg *= -1

    ans += list(range(k + 2, n + 1))
    printList(ans)


solve()
