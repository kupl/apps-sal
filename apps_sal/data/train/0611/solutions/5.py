
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 ln1=len(set(l))
 l1=[]
 for i in l:
  l1.append(l[i-1])
 ln2=len(set(l1))
 if(ln1==ln2):
  print("Poor Chef")
 else:
  print("Truly Happy")

