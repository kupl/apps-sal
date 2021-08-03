for _ in range(int(input())):
    n, m = map(int, input().split())
    print("YES") if n % 2 == 0 or m % 2 == 0 else print("NO")
