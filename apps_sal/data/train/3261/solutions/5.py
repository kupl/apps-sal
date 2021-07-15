def sort_poker(john, uncle):
    res=[]
    index=0
    while True:
        try:
            temp=john[index]+john[index+1]
            if john[index+1]=="1":
                temp+=john[index+2]
                index+=3
            else:
                index+=2
            res.append(temp)
            temp=""
        except:
            break
    dict={}
    for i in "SDHC":
        dict[i]=uncle.index(i)
    rec="2 3 4 5 6 7 8 9 10 J Q K A"
    dict2={}
    for i,j in enumerate(rec.split()):
        dict2[j]=i
    for i,j in enumerate(res):
        res[i]=list(j)
        if len(res[i])==3:
            res[i][1]=res[i][1]+res[i][2]
            res[i].pop()
    for i in range(len(res)):
        for j in range(i+1,len(res)):
            if dict2[res[j][1]]<dict2[res[i][1]]:
                temp=res[i]
                res[i]=res[j]
                res[j]=temp
    final=sorted(res, key=lambda x: (dict[x[0][0]]))
    return "".join(sum(final, []))
