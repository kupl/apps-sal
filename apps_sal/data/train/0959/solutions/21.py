for _ in range(int(input())):
 n = int(input())
 nums = sorted(list(map(int, input().split())))
 
 res = sum(nums[n//2:]) - sum(nums[:n//2])
 print(res)
