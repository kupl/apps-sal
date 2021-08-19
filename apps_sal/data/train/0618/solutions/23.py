for k in range(int(input())):
    (num, bags) = map(int, input().split())
    coins = list(map(int, input().split()))
    most = 0
    temp = sum(coins[:bags])
    for i in range(num):
        if i + bags <= num:
            temp = temp - coins[i] + coins[(i + bags) % num]
        else:
            temp = temp - coins[i] + coins[(i + bags) % num]
        if temp > most:
            most = temp
    print(most)
