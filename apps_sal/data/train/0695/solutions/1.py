# cook your dish here
tc=int(input())
for j in range(tc):
 ip=list(map(int,input().rstrip().split()))
 x=ip[0]
 y=ip[1]
 n=ip[2]
 cnt=0
 if(x==y):
  print('0')
  continue
 ln=bin(x).replace("0b", "") 
 rn=bin(y).replace("0b", "") 
 ll=len(ln)
 rl=len(rn)
 #print(ln)
 #print(rn)
 if(ll==len(rn)):
  for i in range(ll):
   
   if(ln[i]!=rn[i]):
    ln=ln[i:]
    rn=rn[i:]
    break
 #print(ln)
 if(ln[0]=='0'):
  ln=ln[1:]
  ll-=1
 #print(rn)
 if(rn[0]=='0'):
  rn=rn[1:]
  rl-=1
 ll=len(ln)
 rl=len(rn)
 if(ll>rl):
  lb=ll 
 else:
  lb=rl 
 pl=2**lb 
 hpl=pl//2
 amn=((n+1)//pl)*hpl 
 rm=(n+1)%pl 
 if((rm*2)<=pl):
  amn+=rm
 else:
  amn+=hpl 
 #print("amn = ",amn)
 aln=(n+1)-amn
 #print("aln = ",aln)
 if(x<y):
  print(amn)
 else:
  print(aln)
