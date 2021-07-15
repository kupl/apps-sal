n = int(input())
prime = [False] * (n + 1)
ans = []
for i in range(2, n + 1):
 if prime[i]:
   continue
 x = i
 while x <= n:
   ans.append(x)
   prime[x] = True
   x *= i
 x = i
 while x <= n:
   prime[x] = True
   x += i   

print(len(ans))
for x in ans:
  print(x, end= " ")
 
