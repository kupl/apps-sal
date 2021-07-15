def amb1(s):
    l=list(s)
    s1=s
    l1=list(s1)
    while "kh" in s1:
        l1=list(s1)
        for i in range(len(l1)-1):
            if l1[i]=='k' and l1[i+1]=='h':
                l1=l1[:i]+l1[i+1:]
                s1=''.join(l1)
                break
    return ''.join(l1)
def amb2(s):
    l=list(s)
    s1=s
    l1=list(s1)
    while "u" in s1:
        l1=list(s1)
        for i in range(len(l1)):
            if l1[i]=='u':
                l1=l1[0:i]+['o','o']+l1[i+1:]
                s1=''.join(l1)
                #print(s1)
                break
    return ''.join(l1)
n=int(input())
l=[]
for i in range(n):
    s=str(input())
    while "kh" in s or "u" in s:
        if "kh" in s:
            s=amb1(s)
        if "u" in s:
            s=amb2(s)
    l.append(s)
ll=set(l)
print(len(ll))
