# cook your dish here
def atharva(a:list,n:int): 
 msf = mh = a[0]
 for i in range(n):
  mh = max(a[i],mh+a[i])
  msf = max(msf,mh)
 return msf

n,x = map(int,input().split())
a = list(map(int,input().split()))
summ = sum(a)
max_sum = atharva(a,len(a))
print(summ - max_sum + max_sum/x)
