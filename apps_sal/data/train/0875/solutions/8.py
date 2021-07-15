T = int(input())

for a in range(T):
 n, z1, z2 = map(int,input().split())
 num = [int(a) for a in input().split()][:n]
 num2 = [-1*i for i in num]
 nums = num+num2

 flag = 0
 for val in nums:
  if val == z1 or val == z2:
   flag = 1
   print(1)
   break
 cnt = 0
 for val1 in nums:
  if val1 - z1 in nums or val1 - z2 in nums:
   cnt += 1
 if cnt == len(nums) and not flag == 1:
  flag = 2
  print(2)
 if flag == 0:
  print(0)
