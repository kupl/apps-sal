def array(string):
    newstring = string.strip().split(',')
    l = newstring[1:-1]
    s = ' '.join(l)
    if len(s) == 0:
        print(None)
    else:
        return(s)


#     newstring = string.strip()
#     newstring = (newstring[1:-2].replace(',', ' ')).strip()
#     if len(newstring) == 0:
#         print(None)
#     else:
#         return newstring
