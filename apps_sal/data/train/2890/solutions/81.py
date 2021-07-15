def multiples(m, n):
    multiple=[]
    for x in range(1,m+1):
        multiple.append(x*n)
    return multiple        

print(multiples(5,2.0))
