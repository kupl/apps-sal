for t in range(int(input())):
 k,l,e = list(map(int,input().split()))
 a = list(map(int,input().split()))
 s = float(sum(a)+e)
 if (l/s==int(l/s)):
  print("YES")
 else:
  print("NO")
