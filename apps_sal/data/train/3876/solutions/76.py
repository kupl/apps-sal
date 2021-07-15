def find(n):
    i=1
    count=0
    while i <=n:
        
        #print(i)
        if (i%3)==0 or (i%5)==0:
            count=count+i
        #    print (count)
        i=i+1
    return (count)
