def tidyNumber(n):
    if len(str(n)) == 1:
        return True
    else:
        for i in range(0,len(str(n))-1):
            if int(str(n)[i]) > int(str(n)[i+1]):
                return False
        return True
