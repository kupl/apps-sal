for t in range(int(input())):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    l = [x + k for x in l]
    count = 0
    for i in l:
        if i % 7 == 0:
            count += 1
    print(count)
