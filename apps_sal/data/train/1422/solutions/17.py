for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    ans = n

    for i in range(n):
        if s[i] == '1':
            ans -= 1
        elif i != 0 and s[i - 1] == '1':
            ans -= 1
        elif i != n - 1 and s[i + 1] == '1':
            ans -= 1

    print(ans)
