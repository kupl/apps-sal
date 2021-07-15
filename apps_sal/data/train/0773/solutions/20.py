



for _ in range(int(input())):

    n=int(input())
    #w=[int(x) for x in input().split()]
    a=list(range(1,n+1))
    if n%2==0:
      for i in range(0,n,2):
         a[i],a[i+1]=a[i+1],a[i]
    else:
       
       for i in range(0,n-1,2):
          a[i],a[i+1]=a[i+1],a[i]
       
       a[-1],a[-2]=a[-2],a[-1] 

    for x in a:
    	print(x,end=" ")
    print()


