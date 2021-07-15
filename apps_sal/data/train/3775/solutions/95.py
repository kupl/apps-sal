def digits(n):
    # your code here
    count = 1
    while(n>=10):
        q = n/10
        count += 1
        n = q
        
    return count
