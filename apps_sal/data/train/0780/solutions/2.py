for i in range(eval(input())):
 s = input().split(" ")
 n = int(s[0])
 m = int(s[1])
 if (n%m)%2 == 0:
  print("EVEN")
 else:
  print("ODD")

