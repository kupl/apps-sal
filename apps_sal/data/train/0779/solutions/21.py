for _ in range(int(input())) :
 n = int(input())
 nums = list(map(int,input().split()))
 nums.sort()
 ans = nums[n-1]
 for i in range(2,n+1):
  ans += nums[n-i]
  ans /= 2
 print(ans)
