def palindrome(num):
    if not str(num).isdigit():
        return "Not valid" 
    
    if type(num) == str:
        return "Not valid"
    
    num = str(num)
    
    return num == num[::-1]
    # Code here

