def pattern(n):
    # Happy Coding ^_^
    result = []
    
    #If it's one return nothing
    if n == 1:
        return ''

    #just go through n printing the not odd numbers 
    for i in range(n+1):
           if i%2 == 0:
               result.append(str(i)*i + '\n')
            
    return ''.join(result).strip()

