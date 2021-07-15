for _ in range(int(input())):
    n = int(input())
    ans = n + n//9
    if n % 9 == 0:
        ans -= 1
    print(ans)
