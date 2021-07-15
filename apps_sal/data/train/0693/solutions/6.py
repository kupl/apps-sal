for _ in range (int(input())):
    n = int(input())
    fact = 1
    if n==1:
        print(1)
    else:
        for i in range (n,1,-1):
            fact *= i 
        print(fact)

