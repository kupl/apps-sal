def split(word): 
    return [char for char in word]        

def reverse_number(n):
    isNegative = False
    if n < 0:
        isNegative = True
    output = ""
    stringLst = split(str(n))
    stringLst.reverse()    
    
    for i in stringLst:
            output += i
        
    if (isNegative):
        output = output.replace('-', '')
        result = int(output)
        return result*-1
        
    else:
        return int(output)
