while int(input()) != 0:
 l = list(map(int,input().split()))
 invArray = [0 for j in range(len(l))]
 for i in range(len(l)):
  invArray[l[i]-1] = i + 1
 if invArray == l:
  print("ambiguous")
 else:
  print("not ambiguous") 

