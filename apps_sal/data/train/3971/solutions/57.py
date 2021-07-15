def tidyNumber(n):
    
    return all(map(lambda x: int(str(n)[x]) >= int(str(n)[x-1]), range(1,len(str(n)))))
