def digit(x):
 ans = None
 for i in range(64):
  if x&(1<<i): 
   return i
  
#data = open("P7.txt")
n = int(input())
#n = int(data.readline())
if n<4:
 print("No")
 
else:
 count = [0]*65
 nums = {}
 vals = list(map(int,input().split()))
 #vals = map(long,data.readline().split())
 nums[vals[0]] = 1
 prebit = 999999999
 
 for i in range(1,n):
  bit = digit(vals[i]^vals[i-1])
  if bit!=prebit:
   count[bit] += 1
   prebit = bit
  try:
   nums[vals[i]] += 1
  except:
   nums[vals[i]] = 1
  
 m1 = max(count)
 m2 = max(nums.values())
 if m1>=2 or m2>=4: print("Yes")
 else: 
  num_doubles = 0
  for val in list(nums.values()):
   if val >= 2:
    num_doubles += 1
  if num_doubles >= 2:
   print("Yes")
  else:
   print("No")
