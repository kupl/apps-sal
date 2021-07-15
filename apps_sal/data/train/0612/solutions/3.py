# cook your dish here
for _ in range(int(input())):
 bstr = input()
 # if '101' in bstr or '010' in bstr:
 #     print("Good")
 # else:
 #     print("Bad")
 opval = "Bad"
 for i in range(len(bstr)-2):
  if bstr[i] == bstr[i+2] and bstr[i]!=bstr[i+1]:
   opval = "Good"
   break
 print(opval)
