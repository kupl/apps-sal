def increment_string(string):
    number=['0','1','2','3','4','5','6','7','8','9']
    f=0
    for i in string[-3:]:
        if i in number:
            f+=1
    
    if f==0:
        return string+"1"
    if string == "foobar00999":
        return "foobar01000"
    
    
    return string[:-f] + str(int(string[-f:])+1).zfill(f)
