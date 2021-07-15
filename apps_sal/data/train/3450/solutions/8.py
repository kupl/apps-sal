def array(string):
    if len(string.split(","))>2:
        return(str(' '.join(string.split(',')[1:-1])))

