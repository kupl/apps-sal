import re
def frogify(s): 
    print(s)
    s =re.sub("\s?[(),\[\];{}-]+",r"",s)
    print(s)
    match =re.findall("\w[\w, -]+",s)
    for i in match:
        print(i)
        rev = " ".join(reversed(i.split()))
        s = re.sub(i,rev,s)
    return s.lstrip()
    

