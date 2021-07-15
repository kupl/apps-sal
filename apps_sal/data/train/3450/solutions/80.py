def array(string):
    print(string)
    if len(string.split(',')) <= 2:
        return None
    else:
        listed = string.split(',')
        print((listed[1:][:-1]))
        listed = listed[1:][:-1]
        return ' '.join(listed)
    

