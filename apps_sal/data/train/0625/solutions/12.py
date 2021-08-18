for _ in range(int(input())):
    N = int(input())
    seq = list(map(int, input().split()))
    count = {0: 1}
    total = 0
    summ = 0
    for i in range(N):
        summ += seq[i]
        r = summ % (10**9)
        if count.get(r, 0):
            total += count[r]
            count[r] += 1
        else:
            count[r] = 1
    print(total)
