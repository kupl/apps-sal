t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    count = 1
    i = 0
    cum_sum = arr[0]
    while cum_sum < n - 1 - i:
        temp = cum_sum
        for x in range(i + 1, i + 1 + temp):
            cum_sum += arr[x]
        i += temp
        count += 1
    print(count)
