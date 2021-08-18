try:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        l = list(map(int, input().split()))
        count = 0
        for i in l:
            if((i + k) % 7 == 0):
                count += 1
        print(count)
except:
    pass
