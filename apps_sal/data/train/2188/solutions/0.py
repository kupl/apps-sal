from sys import stdin


def main():
    cnt = [0] * 2 ** 18
    t = str.maketrans('0123456789', '0101010101')
    (_, *l) = stdin.read().splitlines()
    for (sign, s) in map(str.split, l):
        if sign == '?':
            print(cnt[int(s, 2)])
        else:
            cnt[int(s.translate(t), 2)] += 1 if sign == '+' else -1


def __starting_point():
    main()


__starting_point()
