# cook your dish here
def fun(s):
    bal=0
    maxbal=0
    for i in range(len(s)):
        if s[i]=='(':
            bal+=1
        else:
            bal-=1
        maxbal=max(maxbal,bal)
    return maxbal
t=int(input())
while t>0:
    s=input()
    maxbal=fun(s)
    print('('*maxbal+')'*maxbal)
    t-=1
