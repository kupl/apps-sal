t = int(input())
for x in range(0, t):
    (n, k, d) = list(map(int, input().split()))
    noofq = list(map(int, input().split()))
    sum1 = 0
    poss = 0
    for j in range(n):
        sum1 = sum1 + noofq[j]
    if sum1 >= k:
        poss = sum1 // k
    else:
        poss = 0
    if poss > d:
        poss = d
    print(poss)
