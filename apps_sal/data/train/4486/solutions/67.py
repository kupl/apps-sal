def repeat_it(string,n):
    if type(string) == str:
        newString = ""
        for i in range (n):
            newString += string
        
        return newString
    else:
        return "Not a string"
