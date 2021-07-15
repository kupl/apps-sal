# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 str1 = input().split(' ')
 a = [int(num) for num in str1]
 sum1 = 1
 M = 1000000007
 count=0 
 for i in range(0,len(a)-1,1):
  if bin(a[i] & (~a[i+1])).count("1") > 0:
   count=-1
   break
  count += bin(a[i] & a[i+1]).count("1")
 
 if(count==-1):
  sum1=0 
 else:
  sum1 = (2**count)%M
 print(sum1)

