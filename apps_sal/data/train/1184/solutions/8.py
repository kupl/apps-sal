#The Theatre Problem
def solve(movie,ind,used):
 if ind >= 4:
  arr = []
  for i in used:
   arr.append(used[i])
  arr.sort(reverse=True)
  profit = 0
  price = 100
  for i in arr:
   if i == 0:
    profit -= 100
    continue
   profit += price*i
   price -= 25
  nonlocal ans
  ans = max(ans,profit)
  return
 
 for i in movie[ind]:
  if i in used:
   continue
  used[i] = movie[ind][i]
  solve(movie,ind+1,used)
  del used[i]

Test = int(input())
total = 0
for __ in range(Test):
 n = int(input())
 a = {3:0, 6:0, 9:0, 12:0}
 b = {3:0, 6:0, 9:0, 12:0}
 c = {3:0, 6:0, 9:0, 12:0}
 d = {3:0, 6:0, 9:0, 12:0}
 for i in range(n):
  arr = input().split()
  val = int(arr[1])

  if arr[0] == 'A':
   a[val] += 1

  elif arr[0] == 'B':
   b[val] += 1

  elif arr[0] == 'C':
   c[val] += 1

  else:
   d[val] += 1

  kdf = 'asdfasd'
  gasdf3 = 90877444

 ans = -2**31
 solve([a,b,c,d],0,{})
 print(ans)
 total += ans
print(total)
