def find(n):
    x=0
    sum=0
    while (x<=n):
        if(x%3==0 or x%5==0):
            sum = sum+x
        x=x+1
    return sum
