t = int(input())
for i in range(t):
    n = int(input())
    matrix = []
    for j in range(n):
        a = list(map(int, input().split(' ')))
        matrix.append(a)
    final_sum = 0
    for k in range(n):
        sum1 = 0
        sum2 = 0
        for p in range(0, k + 1):
            sum1 += matrix[p][n + p - k - 1]
            sum2 += matrix[n + p - k - 1][p]
        sumo = max(sum1, sum2)
        final_sum = max(sumo, final_sum)
    print(final_sum)
