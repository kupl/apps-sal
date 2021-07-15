# cook your dish here
for _ in range(int(input())):
 a=[int(i) for i in input().split()]
 p=a[-1]
 b=[p*i for i in a[:-1]]
 if sum(b)<=120:
  print("No")
 else:
  print("Yes")
