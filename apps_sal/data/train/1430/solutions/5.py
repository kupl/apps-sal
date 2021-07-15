# cook your dish here
# cook your code here
for _ in range(int(input())):
    n,k = map(int,input().split())
    print( (n//2)*(k+2) + (n%2)*(2*k+1)) 
