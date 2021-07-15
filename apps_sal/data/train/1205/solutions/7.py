# cook your dish here
def find2(i):
 ans=0
 return (i+1)*(lenS-i-1)+i*(i+1)/2+(lenS-i-2)*(lenS-i-1)/2
for tests in range(int(input())):
 S=input()
 lenS=len(S)
 ans=0
 for i in range(lenS-1):
  if S[i]==S[i+1]:
   ans+= int(find2(i))
  else:
   ans+=lenS
 print(ans)
