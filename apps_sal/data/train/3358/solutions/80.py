def correct(string):
    if '5' or '0' or '1' in string:      
        string = string.replace('0','O')
        string = string.replace('1','I')
        string = string.replace('5','S')
    return string
