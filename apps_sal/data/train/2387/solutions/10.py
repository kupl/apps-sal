def main():
    for _ in range(int(input())):
        n = int(input())

        ans = 0
        while n > 0:
            ans += n // 10 * 10
            n = n % 10 + n // 10
            if n // 10 < 1:
                break
        ans += n
        print(ans)


main()
