def seven(m):
    temp=str(m)
    count=0
    result=[]
    
    while len(temp)>2:
        calc=int(temp[:-1])-int(temp[-1])*2
        temp=str(calc)
        count+=1
    return int(temp),int(count)
        

