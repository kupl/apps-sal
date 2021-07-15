for _ in range(int(input())):
 n=int(input())
 A=list(map(int,input().split(" ")))
 B=list(map(int,input().split(" ")))
 ans="Yes"

 a_1=A[0]
 a_n=A[n-1]
 b_1=B[0]
 b_n=B[n-1]

 if a_1!=0 or b_n!=0 or a_n!=b_1 :
  ans="No"
 else:
  for i in range(1,n-1):
   if A[i]==0 or B[i]==0 :
    ans="No"
    break
   elif b_1+A[i]<B[i]:
    ans="No"
    break
   elif A[i]+B[i]<b_1:
    ans="No"
    break
   elif B[i]+b_1<A[i]:
    ans="No"
    break
   else:
    pass

 print(ans)
