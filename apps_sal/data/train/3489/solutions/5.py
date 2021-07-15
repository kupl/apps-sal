def save(sizes, hd): 
    ab=0
    sum=0
    for i in sizes:
        sum=sum+i
        if sum > hd:
            return ab
        ab+=1
    print(ab)
    return ab
