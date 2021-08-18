l = [1]
for k in range(31):
    l.append(l[-1] * 2)


def convert(s):
    while len(s) != 32:
        s = '0' + s
    ans = ""
    for i in s:
        ans = i + ans
    return ans


def main():
    for _ in range(int(input())):
        n = int(input())
        val = list(map(int, input().split()))
        p = list(map(float, input().split()))
        res = 0
        for i in range(32):
            x = 0
            for j in range(n):
                if val[j] & (1 << i):
                    x = (p[j] * (1 - x)) + (1 - p[j]) * (x)
            res += (l[i] * x)
        print("%.6f" % res)


def __starting_point():
    main()


__starting_point()
