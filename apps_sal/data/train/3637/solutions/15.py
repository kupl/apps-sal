def num_primorial(n):
    lst=[2]
    for i in range(2,7919):
        count=0
        for e in lst:
            if i%e==0:
                count=count+1
        if count==0:
            lst.append(i)
        if len(lst)==n:
            break

    prod=1
    for e in range(n):
        prod=prod*lst[e]
    return prod  

