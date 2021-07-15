import sys

t = int(input())

while (t):

 line = input().split()
 a,k = int(line[0]),int(line[1])

 line = input().split() 
 arr = [int(line[0]),int(line[1]),int(line[2])]
 arr.sort() 

 start = arr[0] - a/2 - k
 end = arr[0] + a/2 + k
 
 start = max(start,arr[1]-a/2-k)
 end = min(end,arr[1]+a/2+k)
 
 start = max(start,arr[2]-a/2-k)
 end = min(end,arr[2]+a/2+k)

 if (start < end):
  ans = min(end-start,a)*a
 else:
  ans = 0

 sys.stdout.write('%.6f\n' % ans)

 t -= 1

