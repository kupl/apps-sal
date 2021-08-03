def main():
    def plus(a, b):
        if a == "":
            return b
        elif b == "":
            return a
        elif a == "A":
            if b == "A":
                return "B"
            else:
                return ""
        else:
            if b == "A":
                return ""
            else:
                return "A"

    def minus(a, b):
        if b == "A":
            b = "B"
        elif b == "B":
            b = "A"
        return plus(a, b)
    dp1 = [""]
    dp2 = [""]
    s = input()
    t = input()
    q = int(input())
    abcd = [list(map(int, input().split())) for _ in [0] * q]
    for i in s:
        dp1.append(plus(dp1[-1], i))
    for i in t:
        dp2.append(plus(dp2[-1], i))
    for a, b, c, d in abcd:
        a, b, c, d = dp1[a - 1], dp1[b], dp2[c - 1], dp2[d]
        print(["NO", "YES"][minus(b, a) == minus(d, c)])


main()
