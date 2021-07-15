import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n = int(input()) 
#n,x = [int(i) for i in readline().split()]
a = [int(i) for i in readline().split()]

def zeta_transform(a,n): #高速ゼータ変換
    b = [[i,0] for i in a]
    for i in range(n):
        I = 1<<i
        for j in range(1<<n):
            if not j&I:
                if b[j][0] > b[j^I][0]:
                    b[j^I][0],b[j^I][1] = b[j][0], b[j^I][0]
                    if b[j][1] > b[j^I][1]:
                        b[j^I][1] = b[j][1]
                elif b[j][0] > b[j^I][1]:
                    b[j^I][1] = b[j][0]
    return b

#print(a)
za = zeta_transform(a[:],n)
#print(zeta_transform(a[:],n),"zeta-a")

for i, zi in enumerate(za):
    if not i: ans = 0
    else:
        i1,i2 = za[i]
        ans = max(ans,i1+i2)
        print(ans)    



