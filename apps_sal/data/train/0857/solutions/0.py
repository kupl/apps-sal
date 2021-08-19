testcases = int(input())
for i in range(testcases):
    n = int(input())
    my = list(map(int, input().split()))
    opp = list(map(int, input().split()))
    my.sort(reverse=True)
    opp.sort(reverse=True)
    j = 0
    k = 0
    while k < n:
        if my[j] > opp[k]:
            j += 1
        k += 1
    print(j)
