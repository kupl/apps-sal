def pattern(n):
    str2 = ""
    for i in range(1,n+1):
        str2 += '{}\n'.format(str(i) * i) 
    str2 = str2[:-1]
    return str2
