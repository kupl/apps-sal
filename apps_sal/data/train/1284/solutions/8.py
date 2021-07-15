for t in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 i=n//4
 s1=a[0:i]
 s2=a[i:2*i]
 s3=a[2*i:3*i]
 s4=a[3*i:4*i]
 comb=list(set(s1)&set(s2))+list(set(s2)&set(s3))+list(set(s3)&set(s4))
 if(len(comb)==0):
  print(s2[0],s3[0],s4[0])
 else:
  print(-1)
