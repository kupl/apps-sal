T = int(input())
for _ in range(T):
 n = int(input())
 arr = list(map(int, input().split()))
 a = [0 for _ in range(max(arr)+1)]
 star_val = []
 for i in range(len(arr)):
  j = 1
  val = 0
  while j*arr[i] <= len(a):
   val += a[j*arr[i]-1]
   j += 1
  star_val.append(val)
  a[arr[i]-1] += 1
 print(max(star_val))
