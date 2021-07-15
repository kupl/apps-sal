def is_palindrome(string):
    #se for um numero, converte para string
    if isinstance(string, int):
        string = str(string)
      
    result = False
    
    strcmp = string[::-1]
    
    if strcmp == string:
        result = True
    else:
        result = False
        
    return result

