for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    count = pair = 0
    for i in range(n):
        if l[i] % 2 == 0:
            count += 1
        else:
            pair += count
    print(pair)
