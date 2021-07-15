s=input()
for _ in range(int(input())):
 st=input()
 if(s.islower() and st.islower()):
  if(set(st)==set(s)):
   print("Yes")
  else:
   print("No")
 else:
  print("No")

