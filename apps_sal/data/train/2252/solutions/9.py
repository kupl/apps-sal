import sys
input = sys.stdin.readline


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    return a * b / gcd(a, b)


def main():
    comp = []
    c = 1
    for i in range(27):
        comp.append(c)
        c *= 2
    n = int(input())
    d = {}
    table = []
    for i in range(n):
        k = [0] * 27
        s = input()
        for j in s:
            if ord(j) - ord('a') >= 0:
                k[ord(j) - ord('a')] += 1
        key = 0
        for i in range(26):
            if k[i] % 2:
                key += comp[i]
        table.append([k, key])
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    ans = 0
    for i in list(d.values()):
        ans += i * (i - 1) // 2
    for i in table:
        for j in range(len(i[0])):
            if i[0][j] % 2:
                if i[1] - comp[j] in list(d.keys()):
                    ans += d[i[1] - comp[j]]
    print(int(ans))
    return


def __starting_point():
    main()


__starting_point()
