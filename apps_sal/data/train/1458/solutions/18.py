# cook your dish here
for _ in range(int(input())):
 n=int(input())
 count1=0
 for i in range(1,n+1,2):
  k=n-i+1
  count1+=k*k
 print(count1)
