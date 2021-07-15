int_list = lambda s: [int(n) for n in s.split(" ")]
n,m,k = int_list(input())
arr = int_list(input())
operations = [int_list(input()) for _ in range(m)]

incrs = [0]*len(arr)      # Amount to increment running total when traversing arr
freq = [0]*m              # The number of times the corresponding operation is used
                          # stored in the same format as incrs

for _ in range(k):
  l,r = int_list(input())
  freq[l-1] += 1
  if r < len(freq): freq[r] -= 1
  
times = 0                   # number of times to apply current operation
for i, op in enumerate(operations):
  l,r,d = op
  times += freq[i]          # update running total
  incrs[l-1] += times*d     # encode operation in incrs
  if r < len(incrs): incrs[r] -= times*d
    
prev = 0
for i,n in enumerate(arr):
  arr[i] = prev + n + incrs[i]
  prev += incrs[i]
  
print(" ".join([str(n) for n in arr]))
