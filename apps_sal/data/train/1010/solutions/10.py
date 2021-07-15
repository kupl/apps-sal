for t in range(int(input())):
 n, k = list(map(int, input().split()))
 poles = list(map(int, input().split()))
 dist = list(map(int, input().split()))
 pd = []
 for i in range(1,n):
  pd.append(poles[i]-poles[i-1])
 c = 0
 for i in range(n-k):
  if (pd[i]==dist[0]):
   temp = pd[i:i+k]
   if (temp == dist):
    c+=1
 print(c)
