T = int(input())
for _ in range(T):
 n = int(input())
 l = list(map(int, input().split()))
 even, odd = [], []
 for num in l:
  if num%2 == 0:
   even.append(num)
  else:
   odd.append(num)
 print(len(even)*len(odd))
