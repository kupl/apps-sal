for _ in range(int(input())):
 n, k = map(int, input().split())
 arr= list(map(int, input().split()))
 motu, tomu = [], []
 for i in range(n):
  if i%2 == 0:
   motu.append(arr[i])
  else:
   tomu.append((arr[i]))
 motu.sort(reverse=True)
 tomu.sort()
 for i in range(len(motu)):
  if len(tomu)-1<i:
   break
  if k==0:
   break
  if tomu[i]<motu[i]:
   tomu[i], motu[i] = motu[i], tomu[i]
   k-=1
 if sum(tomu) > sum(motu):
  print("YES")
 else:
  print("NO")
