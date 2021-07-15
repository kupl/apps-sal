def main():
    s = input()
    n = int(input())
    
    M = 1000000007
    a = {str(s):[10, s] for s in range(10)}
    d = [['_', s]] + [input().split('->') for _ in range(n)]
    
    for di, ti in reversed(d):
        _p = 1
        _v = 0
        for c in ti:
            _v = (_v * a[c][0] + a[c][1]) % M
            _p = (_p * a[c][0]) % M
        a[di] = [_p, _v]

    print(a['_'][1])

    
def __starting_point():
    main()


__starting_point()
