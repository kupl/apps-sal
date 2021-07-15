# cook your dish here
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
t=int(input())
for i in range(0,t):
    n=int(input())
    if n==1:
        print("2")
        continue
    if isPrime(n):
        print(n+1)
        continue
    if n%2==0:
        k=n//2
        min=2+k
    else:
        min=n+1
    for j in range(2,(n//2)+1):
        if n%j==0:
            k=n//j
            if k!=j:
                l=j+k
                if l<min:
                    min=l
    print(min)

