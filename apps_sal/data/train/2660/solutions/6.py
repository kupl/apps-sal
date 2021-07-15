def args_to_string(args):
    ls=[]
    for i in args:
        if type(i)==list and len(i)==2:
            if len(i[0])>1:
                i[0]='--'+i[0]
                ls.extend(i)
            else:
                i[0]='-'+i[0]
                ls.extend(i)
        else:
            ls.append(i) if type(i)!=list else ls.extend(i)
    return ' '.join(ls)

