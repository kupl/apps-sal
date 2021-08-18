for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    coins = input().split()
    count = 0

    for i in range(k):
        coin = coins.pop()

        if coin == 'H':
            count += 1
            coins = ['T' if val == 'H' else 'H' for val in coins]

    res = coins.count('H')

    print(res)
