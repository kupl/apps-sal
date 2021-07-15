def main():
    import sys
    input = sys.stdin.readline

    a = list(input())[:-1]
    #print(a)
    n = len(a)

    d = dict()
    for i in range(26):
        d[chr(i+97)] = chr(i+97)
    

    for i in range(n-1,-1,-1):
        min_key = 'zz'
        min_len = 10**9
        for e in d:
            if (min_len == len(d[e]) and min_key > e) or (min_len > len(d[e])):
                min_key = e
                min_len = len(d[e])
        d[a[i]] = a[i]+d[min_key]

    res_len = len(d['a'])
    res_key = 'a'
    for e in d:
        if (res_len == len(d[e]) and res_key > e) or (res_len > len(d[e])):
            res_key = e
            res_len = len(d[e])
    print(d[res_key])

def __starting_point():
    main()
__starting_point()
