#  =========     /\       /|    |====/|
#      |        /  \       |    |   / |
#      |       /____\      |    |  /  |
#      |      /      \     |    | /   |
#  ========= /        \  =====  |/====|
#  code

def main():
    t = int(input())
    for _ in range(t):
        a, b, n = map(int, input().split())
        f = [a, b, a ^ b]
        print(f[n % 3])
    return


def __starting_point():
    main()


__starting_point()
