for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    curr = 0
    ans = 0
    for x in a:
        curr += x
        ans += abs(curr)
    print(ans)
