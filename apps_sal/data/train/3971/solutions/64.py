def tidyNumber(n):
    for i in range(len(str(n))-1):
          if str(n)[i]>str(n)[i+1]:
                return False 
                break
    return True
          

