T=int(input())
for i in range(0,T):
 N=int(input())
 word=input()
 min=word[0]
 for j in range (0,N):
  if (word[j]<=min):
   min=word[j]
 print(min)
