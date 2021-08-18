testCases = int(input())
for c in range(testCases):
    n, k = list(map(int, input().split()))
    sum = 0
    i = 0
    power = 1
    while i <= n:
        if k**power == i:
            power += 1
        else:
            sum += i
        i += 1
    answer = "Case
    print(answer)
