a=[]
def maxx(a,b):
 if(a>b):
  return a;
 return b


def fnd(cur,mx):
 if(cur>mx):
  return 1;
 f=fnd(2*cur,mx)
 g=fnd(2*cur+1,mx)
 return (a[cur]*maxx(f,g));


def main():
 while(1):
  n=eval(input());
  if(n==0 ):
   break
  while(len(a)!=0):
   a.pop();
  a.append(0);
  x=input().split();
  mx=2**n -1;
  for i in range(0,2**n-1):
   a.append(int(x[i]));
  print(fnd(1,mx)%1000000007)


main()

