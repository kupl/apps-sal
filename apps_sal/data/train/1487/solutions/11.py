for _ in range(int(input())):
    N = int(input())
    candies = list(map(int, input().split()))
    x = int(input())
    sum = 0
    for a in range(N):
        sum += candies[a]
    lftSum = candies[0]
    rgtSum = sum - lftSum
    lftans = 1
    rgtans = N - 1
    for a in range(1, N):
        if rgtSum - candies[a] == lftSum / x:
            if lftans >= rgtans - 1:
                lftans += 1
                rgtans -= 1
                break
            else:
                break
        elif rgtSum - candies[a] < lftSum / x:
            break
        else:
            lftans += 1
            rgtans -= 1
        lftSum += candies[a]
        rgtSum -= candies[a]

    print(lftans, rgtans)
