def getPairsCount(arr, n, sum):
 m = [0] * 10000001

 for i in range(0, n):
  m[arr[i]] += 1

 twice_count = 0

 # Iterate through each element and increment
 # the count (Notice that every pair is
 # counted twice)
 for i in range(0, n):

  twice_count += m[sum - arr[i]]

  # if (arr[i], arr[i]) pair satisfies the
  # condition, then we need to ensure that
  # the count is  decreased by one such
  # that the (arr[i], arr[i]) pair is not
  # considered
  if (sum - arr[i] == arr[i]):
   twice_count -= 1

 # return the half of twice_count
 return int(twice_count / 2)
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 su=2000
 val=getPairsCount(l, n, su)
 if(val):
  print("Accepted")
 else:
  print("Rejected")

