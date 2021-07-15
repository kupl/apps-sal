def count_number(n, x):
    #your code here
    return sum(1 for i in range(1,n+1) if x//i in range(1,n+1) and x%i==0) 

