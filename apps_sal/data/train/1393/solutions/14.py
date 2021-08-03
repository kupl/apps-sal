def maxSpeed(arr, l):
    count = 0
    Min = 10000000000000
    for i in arr:
        if i < Min:
            Min = i
            count += 1

    return count


t = int(input())
for i in range(t):
    l = int(input())
    arr = list(map(int, input().split()))
    print(maxSpeed(arr, l))
