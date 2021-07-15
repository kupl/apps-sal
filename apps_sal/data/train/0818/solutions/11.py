for _ in range(int(input())):
 lens=int(input())
 arrs=[int(x) for x in input().split()]
 even=[i for i,x in enumerate(arrs) if x%2==0]
 nbq=int(input())
 for _ in range(nbq):
  answer="ODD"
  l,r=[int(x) for x in input().split()]
  for j in even:
   if(l-1)<=j<r:            
    answer="EVEN"
    break
  print(answer)
