def count_change(N, coins):
    count = [0] * (N + 1)  # counts number of possibilties
    count[0] = 1
    for i in range(len(coins)):
        j = coins[i]
        while j <= N:
            count[j] += count[j - coins[i]]
            j += 1
    return count[N]
