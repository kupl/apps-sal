try:
    for _ in range(int(input())):
        n = int(input())
        d = list(map(int, input().split()))
        s = int(input())
        p = list(map(int, input().split()))
        o = int(input())
        t = list(map(int, input().split()))
        w = int(input())
        q = list(map(int, input().split()))
        l = []
        for i in t:
            if i in d:
                l.append('y')
            else:
                l.append('no')
        for i in q:
            if i in p:
                l.append('y')
            else:
                l.append('no')
        if 'no' in l:
            print('no')
        else:
            print('yes')
except:
    pass
