# cook your dish here
t=int(input())
for i in range(t):
 a=int(input())
 cho =list(map(int, input().split()))
 maxc=max(cho)
 start=cho.index(maxc)
 mid =int(len(cho)/2)
 for j in range(len(cho)-1, 0, -1):
  if(cho[j]==maxc):
   end = j
   break
 ans =((len(cho))-end)-(mid-start)
 print(max(0,ans))
