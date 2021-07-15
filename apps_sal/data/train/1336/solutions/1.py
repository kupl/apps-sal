#!/usr/bin/env python

def main():
    t = 1
    while True:
        x = input()
        if x == '0': break
        A, B = list(map(int, x.split()))
        if A > B: A, B = B, A
        x = ''.join(map(str, range(A, B + 1)))
        x = [(k,x.count(str(k))) for k in range(10)]
        print("Case %s: %s" % (t, ' '.join(["%s:%s" % z for z in x])))
        t += 1

main()


