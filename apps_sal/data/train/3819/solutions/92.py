def smash(words):
    # Begin here
    res = ''
    if len(words) == 1:
        for i in words:
            res = res + i
        return res
    else:

        for i in words:
            res = res +" "+ i 
        return res[1:]
