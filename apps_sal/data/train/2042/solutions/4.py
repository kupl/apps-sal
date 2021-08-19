def main():
    n, a, b, t = list(map(int, input().split()))
    b += 1
    l = [b if char == "w" else 1 for char in input()]
    t -= sum(l) - a * (n + 2)
    hi, n2 = n, n * 2
    n3 = n2 + 1
    lo = res = 0
    l *= 2
    while lo <= n and hi < n2:
        t -= l[hi]
        hi += 1
        while (hi - lo + (hi if hi < n3 else n3)) * a > t or lo < hi - n:
            t += l[lo]
            lo += 1
            n3 -= 1
        if res < hi - lo:
            res = hi - lo
            if res == n:
                break
    print(res)


def __starting_point():
    main()


# Made By Mostafa_Khaled
__starting_point()
