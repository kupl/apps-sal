def alternateCase(s):
    newstring ='' 
    count1 = 0
    count2 = 0
    count3 = 0
    for a in s: 
# Checking for lowercase letter and converting to uppercase. 
        if (a.isupper()) == True: 
            count1+= 1
            newstring+=(a.lower()) 
# Checking for uppercase letter and converting to lowercase. 
        elif (a.islower()) == True: 
            count2+= 1
            newstring+=(a.upper()) 
# Checking for whitespace letter and adding it to the new string as it is. 
        elif (a.isspace()) == True: 
            count3+= 1
            newstring+= a 
    return newstring
