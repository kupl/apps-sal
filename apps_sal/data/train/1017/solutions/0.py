# cook your dish here
for t in range(int(input())):
 a1,a2,a3,a4,a5,p=[int(x)for x in input().rstrip().split()]
 if (a1+a2+a3+a4+a5)*p >120:
  print("Yes")
 else:
  print("No")

