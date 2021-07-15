# cook your dish here
def chocoValue(a,b):
 if a<b:
  a,b=b,a
 if b==0: 
  return a
 return chocoValue(b,a%b)


for x in range(int(input())):
 m,b=map(int,input().split())
 if m or b:
  sumValue= chocoValue(m,b)
  print(2*sumValue)
 else:
  print(0)
