m = 10**9 + 7
for _ in range(int(input())):
 n1,n2,n3 = list(map(int,input().split()))
 ls = [n1,n2,n3]
 ls.sort()
 print( (ls[0]*(ls[1]-1)*(ls[2]-2 ))%m)
 #three different numbers

