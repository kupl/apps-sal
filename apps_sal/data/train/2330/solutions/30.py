import sys


def main():
    s = list(input())
    l = len(s)
    if s[0] != "1" or s[-1] != "0":
        print((-1))
    else:
        for i in range(l // 2):
            if s[i] != s[l - i - 2]:
                print((-1))
                return
        s = s[::-1]
        s[0] = "1"
        now = 0
        ans = []
        while now < l - 1:
            c = 1
            ans.append((l - now, l - (now + c)))
            while s[now + c] == "0":
                c += 1
                ans.append((l - now, l - (now + c)))
            now += c
        for x, y in ans:
            print((x, y))


def __starting_point():
    main()


__starting_point()
