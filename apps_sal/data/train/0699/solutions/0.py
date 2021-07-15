for T in range(int (eval(input()))):
 N,K,D=list(map(int,input().split()))
 A=list(map(int,input().split()))
 P=sum(A)//K 
 print(min(P,D))

