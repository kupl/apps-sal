def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        n, x = list(map(int, stdin.readline().split()))
        a = set(map(int, stdin.readline().split()))
        max_a = max(a)
        ans = (x - 1) // max_a + 1
        if ans == 1 and x not in a:
            ans = 2
        print(ans)


main()
