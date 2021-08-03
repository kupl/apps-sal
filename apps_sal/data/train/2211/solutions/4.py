t = int(input())
for _t in range(t):
    n, x = map(int, input().split())
    nums = list(map(int, input().split()))

    print(min((x + m - 1) // m if m <= x else 2 for m in nums))
