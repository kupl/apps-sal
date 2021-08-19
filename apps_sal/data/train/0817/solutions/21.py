for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    ans = 0
    for i in l:
        ans ^= i
    print(ans)
