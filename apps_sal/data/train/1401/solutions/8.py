# cook your dish here
n,p=list(map(int,input().split()))
li=list(map(int,input().split()))
li.sort()
s=i=c=0
while p>=s:
 s+=li[i]
 c+=1
 if s>p:
  c-=1
  break
 i+=1
print(c)

