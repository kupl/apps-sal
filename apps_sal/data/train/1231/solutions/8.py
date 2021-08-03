#!/usr/bin/env python

T = int(input())
for t in range(T):
    N = int(input())
    print(sum(map(int, str(2**N))))
    '''
    X = 2**N
    print '2^%d=%d' % (N, X)
    X = map(int, str(X))
    print '%s=%d' % ('+'.join(map(str, X)), sum(X))
    '''
