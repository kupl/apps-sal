testcases = int(input())

for _ in range(testcases):
    total_islands = int(input())

    coins_list = list(map(int, input().split()))

    total_trips = int(input())

    for _ in range(total_trips):
        coins = 0

        (start, end) = list(map(int, input().split()))

        for i in range(start - 1, end):
            coins = coins + coins_list[i]

        print(coins)
