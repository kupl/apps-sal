import bisect
n = int(input())
x = list(map(int, input().split()))
l = int(input())
q = int(input())
query = [list(map(int, input().split())) for i in range(q)]
log_size = n.bit_length() + 1
double = [[0] * n for i in range(log_size)]
for i in range(n):
    double[0][i] = bisect.bisect_right(x, x[i] + l) - 1
for k in range(1, log_size):
    for i in range(n):
        double[k][i] = double[k - 1][double[k - 1][i]]
for (a, b) in query:
    a -= 1
    b -= 1
    if a > b:
        (a, b) = (b, a)
    ans = 10 ** 18
    tmp = 0
    for k in range(log_size)[::-1]:
        if double[k][a] >= b:
            ans = min(ans, 2 ** k + tmp)
        else:
            a = double[k][a]
            tmp += 2 ** k
    print(ans)
