
def fac(x):
    x=len(x)
    return int(((x-1)*(x))/2)


t= int(input())
for o in range(t):
    n=int(input())
    s=input()
    a=s.split("1")
    a="".join(a)
    b=s.split("0")
    b="".join(b)
    print(fac(s)-fac(a)-fac(b),)

