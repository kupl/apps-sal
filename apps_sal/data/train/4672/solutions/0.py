import re
def AlphaNum_NumAlpha(string):
    return re.sub( r'[0-9]{1,2}|[a-z]', lambda x:str(ord(x.group() )-96) if x.group().isalpha() else chr(int(x.group())+96)  , string)
    
    #\w

