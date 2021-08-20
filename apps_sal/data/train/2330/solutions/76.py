import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10 ** 9))


def write(x):
    return sys.stdout.write(x + '\n')


s = input()
n = len(s)
if s[0] == '0' or s[-2] == '0' or s[-1] == '1':
    print('-1')
elif any((s[i] != s[-2 - i] for i in range(n - 1))):
    print('-1')
else:
    i = 1
    ps = set([i])
    es = []
    for c in s[1:]:
        i += 1
        if c == '0':
            ps.add(i)
        else:
            for u in ps:
                es.append('%s %s' % (u, i))
            ps = set([i])
    for u in ps:
        if u != n:
            es.append('%s %s' % (u, n))
    write('\n'.join(es))
