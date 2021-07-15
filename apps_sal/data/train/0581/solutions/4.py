for __ in range(eval(input())):
 k, l, e = list(map(int,input().split()))
 arr = list(map(int, input().split()))
 val = sum(arr) + e
 if l%val ==0:
  print("YES")
 else:
  print("NO")

