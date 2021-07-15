

def main():
  t=int(input())
  while t :
    t=t-1
    n,m=input().split()
    x=100*[0]
    for i in range(int(n)):
      y=input().split()
      c=int(y[0])
      l=int(y[1])
      x[l-1]=x[l-1]+c
    z=100*[0]
    for i in range(int(m)):
      y=input().split()
      c=int(y[0])
      l=int(y[1])
      z[l-1]=z[l-1]+c
    s=0
    for i in range(100):
      if z[i]>x[i] :
        s=s+(z[i]-x[i])
    print(s)
    

def __starting_point():
  main()
__starting_point()
