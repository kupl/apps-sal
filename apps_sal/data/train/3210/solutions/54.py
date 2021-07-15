def get_strings(city):
    a=[]
    b=[]
    for i in city.lower(): 
        if i==" ": continue
        if i in a:
            continue
        a+=[i]
        b+=[str(i)+":"+"*"*city.lower().count(i)]
    return ",".join(b)
