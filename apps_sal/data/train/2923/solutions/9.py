def dad_filter(string):
    #your code here
    new_list = string.split()
    for i in range(len(new_list)):
        while new_list[i].count(',') > 1:
            new_list[i] = new_list[i].replace(',', '', 1)
    
    str = ' '.join(new_list)       
    while str[-1] in ' ,':
        str = str[:-1]
    return str
