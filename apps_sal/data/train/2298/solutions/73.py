def main():
    (N, T, *A) = map(int, open(0).read().split())
    (cur, cand) = (A[0], [])
    for i in A:
        if i < cur:
            cur = i
        else:
            cand += [i - cur]
    x = max(cand)
    ans = sum((i == x for i in cand))
    print(ans)


def __starting_point():
    main()


__starting_point()
