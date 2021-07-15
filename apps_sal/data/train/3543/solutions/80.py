import re

def increment_string(strng):
    digits_regex = "\d+$"
    value_regex = "[1-9]+$"
    
    ret_str = ""
    
    #any digits on the end of the string
    digits_match = re.search(digits_regex, strng)
    if digits_match:
        digits = digits_match.group(0)
        print(digits)
        #add non-digit characters to return string
        substr = strng[0 : strng.index(digits)]
        ret_str += substr
        #non-zero digits on the end of the string
        value_match = re.search(value_regex, digits)
        if value_match:
            value = value_match.group(0)
            print(value)
            #split off zeros
            leading_zeros = digits[0 : digits.rfind(value)]
            #check if value contains only 9s. This number will roll over to use an 
            #additional digit when 1 is added
            if value.count("9") == len(value):
                leading_zeros = leading_zeros[0 : -1]
            ret_str += leading_zeros
            #add 1 to non-zero number
            value = str(int(value) + 1)
            ret_str += value
        else:
            #remove the last zero when there are only zeros and replace with "1"
            digits = digits[0 : -1] + "1"
            ret_str += digits
    else:
        #string does not end with and digits, therefore append "1"
        ret_str = strng + "1"
    
    return ret_str
                
            
    

