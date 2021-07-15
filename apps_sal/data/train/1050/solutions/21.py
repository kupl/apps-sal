def solve(S):
  mystack = []
  ans = 0
  for i in range(len(S)):
    if(S[i] == "<"):
      mystack.append("<")
    else:
      if(len(mystack) == 0):
        return ans
      else:
        mystack.pop()
        if(len(mystack) == 0):
          ans = i+1
  return ans

  
T = int(input())

for j in range(T):
  print(solve(input()))
