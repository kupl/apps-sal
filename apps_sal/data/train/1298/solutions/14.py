for L_I in range(eval(input())):
 num=eval(input())
 ok=0
 a=list(map(int,input().split()))
 for I_I in range(1,len(a)):
  if a[0]==a[I_I]:
   ok=ok+1
 print(num-ok)

