# cook your dish here
def solution(b,n1,d):
 first=b[0]
 b.sort()
 for j in range(n1-1):
  if(a[j+1]-a[j]>d):
   return "NO"
 for j in range(n1):
  if(b[j]==first):
   pos=j
 if(pos==0 or pos==n1-1):
  return "YES"
 rec=1
 for j in range(pos-1,n1-2):
   if(a[j+2]-a[j]>d):
    rec=0
    break
 if(rec):
  return "YES"
 rec=1
 for j in range(pos+1,1,-1):
   if(a[j]-a[j-2]>d):
    rec=0
    break
 if(rec):
  return "YES"
 else:
  return "NO"
 
testcase=int(input())
for i in range(testcase):
 n,d=list(map(int,input().split()))
 a=list(map(int,input().split()))
 print(solution(a,n,d))

