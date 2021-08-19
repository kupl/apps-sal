def main():
    t = int(input())
    for i in range(t):
        N = int(input())
        l = list(map(int, input().split()))
        c = 0
        gcd = 0
        for j in range(min(l), 0, -1):
            c = 0
            for k in l:
                if k % j != 0:
                    break
                else:
                    c += 1
            if c == len(l):
                gcd = j
                break
        cost = 0
        for j in l:
            cost += j // gcd
        print(gcd, cost)


def __starting_point():
    main()


__starting_point()
