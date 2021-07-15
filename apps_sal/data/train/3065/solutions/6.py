def get_textliterals(pv_code):
    r=[]
    i=0
    in_quote=False
    while(i<len(pv_code)):
        if in_quote:
            if pv_code[i]=="'":
                if pv_code[i:].startswith("''"):
                    i+=1
                else:
                    r.append((s,i+1))
                    in_quote=False
        else:
            if pv_code[i]=="'":
                s=i
                in_quote=True
            elif pv_code[i:].startswith('--'):
                i=pv_code.index('\n',i)
            elif pv_code[i:].startswith('/*'):
                i=pv_code.index('*/',i+2)
                i+=1
        i+=1
    if in_quote:
        r.append((s,len(pv_code)))
    return r
