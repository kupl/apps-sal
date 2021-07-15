def is_palindrome(s):
    
    p1=0 #Pointer 1 starts beginning of string
    p2=len(s)-1 #Pointer 2 starts at end of string
    
    while p1<p2: #While the first pointer is less than the second
        
        #Compares the values of first and last characters in string
        if s[p1].lower()==s[p2].lower():  
            p1+=1 #Increases position of pointer 1 
            p2-=1 #Decreases position of pointer 2
            continue
        
        else: #Returns false if the values do not match
            return False
    
    return True #If while loop is broken, returns true

