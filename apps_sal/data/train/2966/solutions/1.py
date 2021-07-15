import re
def calculate(string):
    x,y=re.findall('\d+',string)
    if re.search('loses', string): s= int(x)-int(y)
    if re.search('gains', string): s= int(x)+int(y)
    return s
