def find(n):
    sum=0
    for x in range(n):
        if (x%3 == 0 or x%5 == 0):
            sum += x
    if(n%3 == 0 or n%5==0):
        return sum + n
    else:        
        return sum

print(find(5))
