# cook your dish here
def main(): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    # all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    n=1000000
    prime = [True for i in range(n + 1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    # Print all prime numbers 
    s=[]
    s.append(0)
    for p in range(1,n + 1): 
        if prime[p]: 
            s.append(s[p-1]+(p))
        else:
            s.append(s[p-1])
    # print(s)
    t=int(input())
    for _ in range(t):
        num=int(input())
        print(s[num]%10)
main()
