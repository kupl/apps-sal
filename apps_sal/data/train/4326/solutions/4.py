def london_city_hacker(journey): #Jai Shree Ram
    total=0.0
    l=[]
    for i in range(len(journey)):
        if type(journey[i])==str:
            total+=2.40
        else:
            if i<len(journey)-1 and type(journey[i+1])==int:
                l.append(journey[i])
                if len(l)==2:
                    total+=1.50 
                    l=[] 
            else:
                total+=1.50
                l=[]
    total=round(total,2)
    return '£'+str(total)+'0'
