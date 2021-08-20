from sys import stdin, stdout
M = 10 ** 8
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list([int(x) // M for x in stdin.readline().split()])
    d = {0: 1}
    s = ans = 0
    for v in a:
        s += v
        req = s % 10
        ans += d.get(req, 0)
        d[req] = d.get(req, 0) + 1
    print(ans)
