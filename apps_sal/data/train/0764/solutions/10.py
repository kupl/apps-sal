# cook your dish here
for _ in range(int(input())):
 a = input().split()
 a = set(a)
 b = set(input().split())
 c = len(a&b)
 if c>=len(a)//2:
  print("similar")
 else:
  print("dissimilar")
