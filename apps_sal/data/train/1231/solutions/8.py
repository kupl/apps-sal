T = int(input())
for t in range(T):
    N = int(input())
    print(sum(map(int, str(2 ** N))))
    "\n    X = 2**N\n    print '2^%d=%d' % (N, X)\n    X = map(int, str(X))\n    print '%s=%d' % ('+'.join(map(str, X)), sum(X))\n    "
