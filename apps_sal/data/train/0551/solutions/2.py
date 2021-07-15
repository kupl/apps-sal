for _ in range(int(input())):
 S = input()
 set_S = list(set(list(S)))
 flag = False
 
 for s in set_S:
  if S.count(s) > 1:
   flag = True
   break
 
 print("yes" if flag else "no")
