def main():
    t = int(input())
    i = 0
    while i < t:
        i = i + 1
        n = int(input())
        ans = pow(3, n - 1, 1000000007) - pow(-1, n - 1, 1000000007)
        print((3 * ans) % 1000000007)
    return 0


main()
