n=int(input())
ah=[]
for _ in range(n):
 cach=list(map(int,input().split()))
 ah.append(cach)
ah.sort(key=lambda x:x[0])
#print(ah)
lmit=-2*(10**9)
chop=0
for i in range(n-1):
 a=ah[i][0]-ah[i][1]
 b=ah[i][0]
 c=ah[i][0]
 d=ah[i][0]+ah[i][1]
 if b<ah[i+1][0] and a>lmit:
  lmit=b
  chop+=1
  #print("first")
 elif d<ah[i+1][0] and c>lmit:
  #print("sec",a,b,c,d,lmit,ah[i+1][0])
  lmit=d
  chop+=1
  #print("sec")
 else:
  lmit=b
 #print(lmit)
print(chop+1)

