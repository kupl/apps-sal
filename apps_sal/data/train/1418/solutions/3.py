for j in range(int(input())):
 n = int(input())
 x = list(map(int,input().split()))
 aman = [0,x[0]]
 for i in range(2,n+1):
  aman.append(max(aman[i-1]+x[i-1]*i,aman[i-2]+x[i-1]*(i-1)+x[i-2]*(i)))
 print(aman[-1])
