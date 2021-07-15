for _ in range(int(input())):
 n = int(input())
 arr = list(map(int,input().split()))

 if n<=62:
  st = set()

  for i in range(n):
   curr = 0
   for j in range(i,n):
    curr = curr|arr[j]

    st.add(curr)
  
  if len(st)==n*(n+1)//2:
   print("YES")
  else:
   print("NO")
   
 else:
  print("NO")
