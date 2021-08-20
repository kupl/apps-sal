def main():
    import sys
    input = sys.stdin.readline
    for _ in range(int(input())):
        S = input().rstrip('\n')
        cnt = 0
        ans = 1
        for s in S:
            if s == 'L':
                cnt += 1
                ans = max(ans, cnt + 1)
            else:
                cnt = 0
        print(ans)


def __starting_point():
    main()


__starting_point()
