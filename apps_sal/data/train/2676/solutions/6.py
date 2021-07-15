def find_needed_guards(k):
    nbsold=0
    i=0
    while i<len(k)-1:
        if k[i]==False and k[i+1]==False:
            nbsold+=1
            i+=1
        i+=1
    return nbsold
    

