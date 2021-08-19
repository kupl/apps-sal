for _ in range(int(input())):
    (n, k) = map(int, input().split())
    li = [int(x) for x in input().split()]
    "'en=li[-1]\n    new=li[:len(li)-1]\n    ma=new[0]+new[1]\n    for i in range(1,len(new)-1):\n        if(new[i]+new[i+1]>ma):\n            ma=new[i]+new[i+1]\n        \n    #new.sort(reverse=True)\n    print(en+ma)"
    su = 0
    st = 0
    end = k - 1
    for i in range(k):
        su += li[i]
    res = su
    for i in range(k, n + k):
        su += li[i % n] - li[(i - k) % n]
        if su > res:
            res = su
    print(res)
