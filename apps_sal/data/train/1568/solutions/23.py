try:
    for _ in range(int(input())):
        n = int(input())
        weights = [int(x) for x in input().strip().split()]
        count = 0
        for x in weights:
            if x >= n / 2:
                count += 1
        print(count)
except:
    pass
