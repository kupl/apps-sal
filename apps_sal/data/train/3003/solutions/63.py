def args_count(*p, **n):
    counter = 0
    for i in p:
        counter +=1
    for z in n:
        counter +=1
    return counter
