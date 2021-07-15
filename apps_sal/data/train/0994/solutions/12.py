cases = int(input())
for v in range(cases):
 a = list(map(int,input().strip().split()))
 n = a[0]
 x = a[1]
 a = list(map(int,input().strip().split()))
 
 cnt = 0

 for i in range(1,n+1):
  if x%i == 0:
   side = i
   subsetsum = []
   left = 0
   right = i-1
   s = sum(a[:right+1])
   subsetsum.append(s)
   while right < n - 1:
    right += 1
    s = s + a[right] - a[left]
    left += 1
    subsetsum.append(s)
    

   
   for r in range(n-side+1):
    if subsetsum[r] >= x:
     continue
    for c in range(n-side+1):
     if subsetsum[r] + subsetsum[c] == x//side:
      cnt += 1

 print(cnt)
   
    
# a = [1,2,3,4,5]
# n = 5
# for i in range(1,6):
#     print(i)
#     left = 0
#     right = i-1
#     subset = []
#     s = sum(a[:right+1])
#     subset.append(s)
#     while right < n-1:
#         right += 1
#         s = s + a[right] - a[left]
#         left += 1
#         subset.append(s)

#     print(subset)

