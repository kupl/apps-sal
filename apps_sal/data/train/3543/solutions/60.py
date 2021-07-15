import re

def increment_string(strng):
    # Reverse the string because I want the digits at the end
    item = strng[::-1]
    pattern = r'\d+'
    number = re.search(pattern, item)
    
    # If theirs a number present in the string
    if number:
        reversed_word = re.split(pattern, item, 1)[1]
        reversed_num = number.group()
        num = reversed_num[::-1]
        if num == "9":
            num = "10"
        elif len(num) > 1:
            length = len(num)
            number = int(num)+1
            number = str(number)
            # Add leading zeros
            num = number.zfill(length)
        else:
            num = int(num)+1
    else:
        return strng+"1"
    
    return reversed_word[::-1]+str(num)
    
                
    
#     return strng

