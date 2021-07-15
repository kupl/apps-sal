def square(n,d):
 if n==1:
  return d*d
 a=""
 for i in range(1,n+1):
  a=a+str(i)
 for i in range(n-1,0,-1):
  a=a+str(i)
 #print a
 return d*d*int(a)

t=eval(input())
p=23
parray=[]
parray.append(1)
for i in range(1,3240001):
 parray.append((parray[i-1]*p)%1000000007)
for x in range(0,t):
 n,d=list(map(int,input().split()))
 '''
    num=int(str(d)*n)
    sq=num**2
    '''
 sq=square(n,d)
 #print "this is a test %d"%sq
 m=len(str(sq))
 #print "length of square = %d"%m
 i=0
 sum=0
 sqArray=list(map(int,list(str(sq))))
 #print sqArray
 while i<m:
  #print "i = %d"%i
  sum = (sum+(sqArray[m-i-1])*(parray[m-i-1]))%1000000007
  i=i+1
 print("%d" %sum)
