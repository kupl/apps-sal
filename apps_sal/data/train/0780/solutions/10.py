TC = int(input())
while TC>0:
 X = list(map(int,input().split()))
 A=X[0]%X[1]
 if (A%2==0): print("EVEN")
 else: print("ODD")
 TC-=1
