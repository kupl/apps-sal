# cook your dish here
def solve(s):
 temp = []
 for c in s:
  if c != '=':
   temp.append(c)
 
 count = 1
 ans = 1
 # print(temp)
 if temp:
  for i in range(1, len(temp)):
   if temp[i] == temp[i-1]:
    count += 1
    # print(i, count)
   else:
    ans = max(ans, count);
    count = 1
  ans = max(ans, count);
  print(ans+1)
 else:
  print(1)
 
n = int(input())
for i in range(n):
 s = input().strip()
 solve(s)
