def res(s):
    if len(s) == 2:
        if s[0] == s[1]:
            print("NO")
        else:
            print("YES")

    elif len(s) % 2 != 0:
        print("NO")

    else:
        c1 = s[0]
        c2 = s[1]
        counte = 0
        counto = 0
        for i in range(2, len(s)):
            if i % 2 == 0 and s[i] != c1:
                counte = 1
                break
            elif i % 2 != 0 and s[i] != c2:
                counto = 1
                break

        if counte == 0 or counto == 0:
            print("YES")

        else:
            print("NO")


def __starting_point():
    t = int(input())
    for _ in range(t):
        stri = str(input())
        res(stri)


__starting_point()
