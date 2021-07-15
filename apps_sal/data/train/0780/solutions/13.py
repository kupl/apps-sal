t = eval(input())
for testCase in range(t):
 inp = input()
 n = int(inp.split(' ')[0])
 m = int(inp.split(' ')[1])
 if ((n%m)%2) == 1:
  print("ODD")
 else:
  print("EVEN")
