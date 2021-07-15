def sharkovsky(a, b): return f(a)<f(b)

def f(n,p=0):
    while n%2==0:
        n>>=1
        p+=1
    return n==1, p*(-1)**(n==1), n
