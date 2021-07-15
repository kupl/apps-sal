# cook your dish here
nums = list(map(int, input().split()))

arr = list(map(int, input().split()))

count = 0
s = []

for item in arr:
 
 count = count ^ item
 s.append(count)
 
for i in range(nums[1]):
 query = int(input())
 
 if query % (nums[0] + 1) == 0:
  print(0)
 else:
  print(s[query % (nums[0] + 1) - 1])

