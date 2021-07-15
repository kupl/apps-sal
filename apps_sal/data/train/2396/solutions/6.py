def want(l,r,depth):

    ret = [0] * 26
    if l + 1 == r:
        ret[ad[s[l]]] += 1

        if alp[depth] == s[l]:
            return 0,ret
        else:
            return 1,ret
    else:

        Lmini , Llis = want(l,(l+r)//2,depth+1)
        Rmini , Rlis = want((l+r)//2 , r , depth+1)

        LL = ((l+r)//2-l) - Llis[depth]
        RR = ((l+r)//2-l) - Rlis[depth]

        for i in range(26):
            Llis[i] += Rlis[i]
        return min(Lmini+RR , Rmini+LL) , Llis

from sys import stdin

alp = "abcdefghijklmnopqrstuvwxyz"
ad = {}
for i in range(26):
    ad[alp[i]] = i

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    s = stdin.readline()

    ans,tmp = want(0,n,0)
    print (ans)

