import sys
def isSubsetSum( se, n,  su):
    
   
    subset = [[0]*(n+1) for i in range(su+1)]
    
    
    for i in range(0,n+1):
      subset[0][i] =1;

   
    for i in range(1,su+1):
      subset[i][0] = 0;

     
    for i in range(1,su+1):
     
       for j in range(1,n+1):
       
         subset[i][j] = subset[i][j-1]
         if (i >= se[j-1]):
           subset[i][j] = subset[i][j] or subset[i - se[j-1]][j-1]
    return subset[su][n]  
       



n,q=[int(i) for i in input().split()]
l=[int(i) for i in input().split()]
while q>0:
    q-=1
    s=[]
    s=[int(i) for i in input().split()]
    if s[0]==3:
        l1=s[1]
        r=s[2]
        w=s[3]
        if isSubsetSum(l[l1-1:r],r-l1+1,w)==True:
           sys.stdout.write( "Yes\n")
        else: sys.stdout.write( "No\n")
    elif s[0]==2:
        l1=s[1]
        r=s[2]
        i=l1-1
        j=r-1
        while i<j:
            l[i],l[j]=l[j],l[i]
            j-=1
            i+=1
    else:
        i=s[1]
        x=s[2]
        l[i-1]=x
   
    
        
