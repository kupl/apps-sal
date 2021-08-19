lookup = {}
for i in range(10):
    for j in range(10):
        start = f'{i}{j}'
        n = int(start)
        s = [0, n]
        seen = {}
        while True:
            x = s[-1]
            if x < 10:
                x = x + s[-2] % 10
            else:
                x = x // 10 + x % 10
            pair = (s[-1], x)
            if pair not in seen:
                s.append(x)
                seen[pair] = len(s)
            else:
                idx = seen[pair] - 1
                prefix = s[2:idx]
                loop = s[idx:]
                lookup[start] = (''.join(map(str, prefix)), ''.join(map(str, loop)))
                break


def find(a, b, n):
    start = f'{a}{b}'[-2:].rjust(2, '0')
    (prefix, loop) = lookup[start]
    s = str(a) + str(b) + prefix + loop
    if n < len(s):
        return int(s[n])
    m = (n - len(s)) % len(loop)
    return int(loop[m])
