from sys import stdin
input=stdin.readline
for _ in range(int(input())):
 n,r,x,y=list(map(int,input().split()))
 if x!=0:
  prev_yrs=list(map(int,input().split()))
 else:
  prev_yrs=[]
 if y!=0:
  plgrsm=list(map(int,input().split()))
 else:
  plgrsm=[]
 prev_yrs.extend(plgrsm)
 non_elig=len(set(prev_yrs))
 elig_scholar=n-non_elig
 if elig_scholar>r:
  print(r)
 else:
  print(elig_scholar)
 
    
   
  

