def okkOokOo(s):
    s = s[:-1].lower().replace('k','1').replace('o','0')
    res = ["".join(x.split(', ')) for x in s.split('? ')]   
    return "".join([chr(int(x,2)) for x in res])
