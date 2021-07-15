import re

string_clean = lambda string : re.sub('\d', '', string)

"""remove all digits from the string"""
    
# \d matches any number 0-9
# re.sub replaces the number/s from the string with ''

