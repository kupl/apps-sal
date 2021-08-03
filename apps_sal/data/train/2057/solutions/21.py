3


def main():
    s = input()

    tpw = [1 for i in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        tpw[i] = (2 * tpw[i - 1]) % (10 ** 9 + 7)

    na = 0
    ans = 0
    for c in s:
        if c == 'a':
            na += 1
        else:
            ans = (ans + tpw[na] - 1) % (10 ** 9 + 7)
    print(ans)


main()
