def check(num1, num2, p, k):
    v = num1 + num2
    v *= num1 * num1 + num2 * num2
    v %= p
    v += p
    v %= p
    return v == k % p


def __starting_point():

    n, p, k = (int(x) for x in input().split())
    idx___number = [int(x) for x in input().split()]

    idx___precount = [((pow(x, 4, p) - k * x) % p + p) % p for x in idx___number]

    met_precount___vals = {}
    ans = 0
    for number, precount in zip(idx___number[::-1], idx___precount[::-1]):
        if precount not in met_precount___vals:
            met_precount___vals[precount] = []
        else:
            for val in met_precount___vals[precount]:
                if check(number, val, p, k):
                    ans += 1
        met_precount___vals[precount].append(number)
    print(ans)


__starting_point()
