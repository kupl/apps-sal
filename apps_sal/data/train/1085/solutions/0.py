d = {}
for i in range(26):
 char = chr(i+ord('a'))
 d[char] = []
for i in range(26):
 char = chr(i+ord('a'))
 temp = list(map(int,input().strip().split()))
 for j in range(26):
  if (temp[j] == 1):
   follow= chr(j+ord('a'))
   d[follow].append(char)
   
def f(char,i,n,count):
 if (i==n):
  return count+1
 else:
  ans = 0
  for c in d[char]:
   ans+=f(c,i+1,n,0)
   ans%=(10**9+7)
  return ans

for q in range(int(input().strip())):
 c, n = input().strip().split()
 n = int(n)
 print(f(c,1,n,0))
