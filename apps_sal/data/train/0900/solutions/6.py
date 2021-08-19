from sys import stdin, stdout
inn = stdin.readline
out = stdout.write
for i in range(int(inn())):
    n = int(inn())
    m = 10 ** 9 + 7
    v = 10 * pow(2, n - 1, m) % m
    out(str(v) + '\n')
