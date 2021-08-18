for i in range(int(input())):
    total_bags = int(input())
    bags_with_weight = list(map(int, input().split()))
    count = 0
    for x in bags_with_weight:
        if x >= total_bags // 2:
            count += 1
    print(count)
