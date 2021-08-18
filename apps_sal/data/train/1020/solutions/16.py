def mixi_game(n, k, arr):
    val = 0
    for i in range(n):
        if i % 2 == 0:
            if val < 0:
                val -= arr[i]
            else:
                val += arr[i]

        else:
            if val < 0:
                val += arr[i]
            else:
                val -= arr[i]

    if k <= abs(val):
        return 1

    else:
        return 2


t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    arr = [int(x) for x in input().split()]
    print(mixi_game(n, k, arr))
