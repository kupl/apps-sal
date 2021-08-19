def powerset(s):
    n = len(s)
    masks = [1 << j for j in range(n)]
    for i in range(2 ** n):
        yield [j + 1 for j in range(n) if masks[j] & i]


def is_power2(num):
    return num != 0 and num & num - 1 == 0


def special(l):
    n = len(l)
    for i in range(n):
        lis = [i + 1]
        yield lis
        for j in range(i + 1, n):
            p = l[j] / l[i]
            if p <= 1 or int(p) != p:
                continue
            lis = [i + 1, j + 1]
            yield lis
            sk = (j + 1) * int(p)
            while sk <= n:
                lis.append(sk)
                sk *= int(p)
                yield lis


def expIndices(l):
    a = list(zip(l, l[1:]))
    if len(a) == 0:
        return True
    else:
        p = a[0][1] / a[0][0]
        if p <= 1 or int(p) != p:
            return False
        for i in range(1, len(a)):
            if a[i][1] / a[i][0] != p:
                return False
        return True


def main():
    for _ in range(eval(input())):
        S = input()
        count = 0
        for i in special(range(1, len(S) + 1)):
            s = [S[j - 1] for j in i]
            if s == s[::-1]:
                count += 1
        print(count)


def __starting_point():
    main()


__starting_point()
