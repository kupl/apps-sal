# cook your dish here
t = int(input())
while t > 0:
 n = int(input())
 ans = (n-1)*(n-1) + n*n*n
 print(ans%1000000007)
 t = t -1;
