def get_sequence(o,s,st=1023456789):
    li = []
    for i in range([st,o][o>0 and o>st],9876543211):
        i = str(i)
        if i[0]!='0' and len(set(i))==10 : li.append(int(i))
        if len(li)==s : break
    return li 
