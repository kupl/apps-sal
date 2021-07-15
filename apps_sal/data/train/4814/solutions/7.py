def is_palindrome(s):
    word = s.lower()   
    l_for = []
    i = 0
    
    for char in s:
        l_for.append(word[i])
        i += 1
        
    l_back = []
    j = -1
    
    for char in s:
        l_back.append(word[j])
        j -= 1
   
    if l_for == l_back:
        return True
    else:
        return False
      
      
is_palindrome('aba')
