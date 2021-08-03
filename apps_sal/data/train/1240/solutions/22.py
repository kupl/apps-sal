for _ in range(int(input())):
    n = int(input())
    arr = list(map(lambda x: int(x) % 6, input().split()))
    ans = sum(arr)
    ans += 6 * arr.count(0)
    print(ans)
