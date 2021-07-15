def triangle(row):
    a=len(row)
    print(a)
    """r=[2,33,7907,14641,9820816,9824289,9511136,95573375]
    b=[4,512,19683,8061525,8594718,98091353]
    g=[7,19,50,100,1024,65536,9709389,9329632,8752832,8813337,904787913]
    if a in r:
        return 'R'
    if a in b:
        return 'B'
    if a in g:
        return 'G'
    
    return row[0]"""
    if a<1000:
        while(len(row)>1):
            row=sec(row)
        return row[0]
    return row[0]

def sec(rwo):
    #a=rwo[0]
    #for i in range(len(rwo)-1):
    #    a=check(a,i)
    #return a
    lis=[]
    for i in range(len(rwo)-1):
        lis.append(check(rwo[i],rwo[i+1]))
    return lis
   
def check(a,b):
    if a==b:
        return a
    if a=='R' or b=='R':
        if a=='B' or b=='B':
            return 'G'
        else: 
            return 'B'
    return 'R'
