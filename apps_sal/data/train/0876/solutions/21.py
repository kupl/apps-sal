for _ in range(int(input())):
    n, x = map(int, input().split())
    candies = list(map(int, input().split()))

    min_candy = min(candies)
    max_candy = max(candies)

    if (max_candy - min_candy) < x:
        print("YES")
    else:
        print("NO")
