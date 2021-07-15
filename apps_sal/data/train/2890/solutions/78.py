def multiples(m, n):
    final=[]
    for num in range(1,m+1): # Iterate between 0 to m multiples
        final.append(n*num)  # append every out to a list
    return final
