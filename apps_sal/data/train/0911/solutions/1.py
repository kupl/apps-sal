def find_upper_bound(arr,key):
 low,high = 0,len(arr)-1
 while low<=high:
  mid = (low+high)//2 
  if arr[mid]==key:return mid
  elif arr[mid]>key and mid-1>=0 and arr[mid-1]<key:return mid 
  elif arr[mid]>key:high = mid - 1 
  else:low = mid + 1 
 return mid 
def get_query(l):
 nonlocal prefix_storer,bin_storer
 ind = find_upper_bound(bin_storer,l)
 surplus = (abs(bin_storer[ind]-l)*ind*ind)%limit 
 return (prefix_storer[ind]-surplus+limit)%limit
def fire_query(l,r):
 return (get_query(r)-get_query(l-1))%limit
golomb,dp,prefix_storer,bin_storer = [],[0,1],[0,1],[0,1]
limit = 10**9+7
for i in range(2,10**6+100):
 dp.append(1 + dp[i-dp[dp[i-1]]])
 bin_storer.append(dp[-1]+bin_storer[-1])
 prefix_storer.append(((prefix_storer[-1] + (dp[-1]*i*i)%limit))%limit)
# print(dp[1:20])
# print(bin_storer[1:20])
# print(prefix_storer[1:20])
# print(get_query(2),get_query(4))
for _ in range(int(input())):
 l,r = map(int,input().split())
 print(fire_query(l,r))
