for _ in range(eval(input())):
 n,k = list(map(int,input().split()))
 a = list(map(int,input().split()))
 elementsNeeded = [pow(2,i) for i in range(k)]
 ans = 0
 for i in elementsNeeded:
  if not(i in a):
   ans += 1
 print(ans)

