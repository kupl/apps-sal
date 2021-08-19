def solve():
    k = int(input())
    a = list(map(int, input().split()))
    for i in range(k):
        n2 = -1
        if a[i] == 1:
            n2 = 3
        elif a[i] == 2:
            n2 = 1
        else:
            b = bin(a[i]).replace('0b', '')
            n = len(b)
            if b[n - 2] == '0':
                b = b[0:n - 2] + '1' + b[n - 1:]
            else:
                b = b[0:n - 2] + '0' + b[n - 1:]
            n2 = int(b, 2)
        if i == k - 1:
            print(n2, end='')
        else:
            print(n2, end=' ')


def __starting_point():
    solve()


__starting_point()
