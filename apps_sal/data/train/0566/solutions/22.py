def solve(s1,s2):
 for i in s1:
  for j in s2:
   if i==j:
    return "Yes"
 return "No"
t=int(input())
for _ in range(t):
 s1=input()
 s2=input()
 print(solve(s1,s2))
