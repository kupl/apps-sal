from bisect import bisect_left, bisect, insort


def main():
    n = int(input())
    s = list(input())
    q = int(input())
    _is = {chr(i): [] for i in range(ord("a"), ord("a") + 27)}
    for i, si in enumerate(s):
        _is[si].append(i)
    for _ in range(q):
        t, i, c = input().split()
        i = int(i) - 1
        if t == "1":
            if s[i] != c:
                index = bisect_left(_is[s[i]], i)
                del _is[s[i]][index]
                insort(_is[c], i)
                s[i] = c
        else:
            c = int(c) - 1
            cnt = 0
            for _isi in list(_is.values()):
                if _isi:
                    is_in = bisect(_isi, c) - bisect_left(_isi, i)
                    if is_in:
                        cnt += 1
            print(cnt)


def __starting_point():
    main()


__starting_point()
