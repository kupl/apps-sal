# ARC063D - 高橋君と見えざる手 / An Invisible Hand (ABC047D)
def main():
    N, T, *A = map(int, open(0).read().split())
    cur, cand = A[0], []
    for i in A:
        if i < cur:  # buy at the most inexpensive place
            cur = i
        else:
            cand += [i - cur]  # sell at higher places
    x = max(cand)  # the highest profits
    # count the number of pairs which produce x
    ans = sum(i == x for i in cand)
    print(ans)


def __starting_point():
    main()


__starting_point()
