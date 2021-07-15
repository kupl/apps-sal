for _ in range(int(input())):
 row,col,k = list(map(int, input().split()))
 fen=0
 garden = [[0 for i in range(col)] for j in range(row)]
 for i in range(k):
  r, c=list(map(int, input().split()))
  garden[r-1][c-1] = 1
 #print(garden)
 for c in range(col):
  for r in range(row):
   if r==0 or r==row-1:
    if garden[r][c]==1:
     fen+=1
     #print(c,r)
   if r!=0 :
    if garden[r][c]!=garden[r-1][c]:
     fen+=1
     #print(c,r)
   if c==0 or c==col-1:
    if garden[r][c]==1:
     fen+=1
     #print(c,r)
   if c!=0 :
    if garden[r][c]!=garden[r][c-1]:
     fen+=1
     #print(c,r)
 '''for r in range(row):
     for c in range(col):
      if c==0 or c==col-1:
       if garden[r][c]==1:
        fen+=1
        #print(c,r)
      if c!=0 :
       if garden[r][c]!=garden[r][c-1]:
        fen+=1
        #print(c,r)'''
 print(fen)# cook your dish here

