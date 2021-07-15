for t in range(eval(input())):
 n=eval(input())
 n-=n%10
 n/=10
 print(n*(n+1)/2*10)
