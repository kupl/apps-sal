# cook your dish here
for _ in range(int(input())):
 n=int(input())
 s1=input()
 s2=input()
 if s1.count('1')==s2.count('1') and s1.count('0')==s2.count("0"):
  print("YES")
 else:
  print("NO")
