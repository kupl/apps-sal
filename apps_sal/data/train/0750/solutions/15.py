while int(input())!= 0:
 x = list(map(int, input().split()))
 y = len(x)
 length = [0]*y
 for i in range(y):
  k = x[i]
  length[k-1] = i+1
 if x == length:
  print("ambiguous")
 else:
  print("not ambiguous")
