def no_repeat(string):
    for e in string:
        if string.count(e)==1: 
            return e 
