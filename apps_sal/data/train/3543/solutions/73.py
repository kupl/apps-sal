def increment_string(strng):
    import re
    a = re.findall(r'\d+',strng)

    if len(a)>0:
        a = a[-1]
        longitud = len(str(a))
        b = int(a)+1
        if longitud > len(str(b)):
            diff = longitud-len(str(b))
            number = str(0)*diff+str(b)
            strng = strng.replace(str(a), str(number))
        else:
            strng = strng.replace(str(a), str(b))
            
        
    else:
        strng = strng+"1"
    return strng

    

