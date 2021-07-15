for k in range(int(input())):
 n=int(input())
 li=list(map(int,input().split()))
 b=[]
 for g in range(len(li)-1):
  b.append(li[g]-li[g+1])
 print(min(b))
