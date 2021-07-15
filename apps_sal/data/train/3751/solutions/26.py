# Author Kim Villatoro
# Turn a given boolean into a "Yes" or "No" response
# This program takes in a boolean

def bool_to_word(boolean): # Method definition
    if boolean == True:# If boolean is True, it returns "Yes"
        return("Yes")
    elif boolean == False: # If boolean is False, it returns "No"
        return("No")
    else: 
        None # Return None
