from sys import stdin, stdout
ans = []
for _ in range(int(stdin.readline())):
    (n, k) = map(int, stdin.readline().split())
    s_h = list(map(int, stdin.readline().split()))
    num = (s_h[0] - 1) // k
    for i in range(1, n):
        num += (s_h[i] - s_h[i - 1] - 1) // k
    ans.append(str(num))
stdout.write('\n'.join(ans))
