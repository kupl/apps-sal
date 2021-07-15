import re
def correct(string):
    string = re.sub('0', 'O', string)
    string = re.sub('5', 'S', string)
    string = re.sub('1', 'I', string)
    
    return string
    

