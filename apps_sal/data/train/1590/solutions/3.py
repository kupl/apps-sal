# cook your dish here
for _ in range(int(input())):
 li=[int(i) for i in input().split()]
 li.sort()
 if (li[0]+li[1]+1)>=li[2]:
  print("Yes")
 else:
  print('No')
