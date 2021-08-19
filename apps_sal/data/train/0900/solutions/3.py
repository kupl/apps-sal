__author__ = 'Prateek'


def test():
    k = int(input())
    ans = pow(2, k - 1, int(10 ** 9 + 7)) * 10 % int(10 ** 9 + 7)
    print(ans)


if __author__ == 'Prateek':
    t = int(input())
    for _ in range(t):
        test()
