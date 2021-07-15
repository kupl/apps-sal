def disarium_number(number):
    b=[]
    a=list(str(number))
    a= [int(x) for x in a]
    
    for i in  range(len(a)) :
        print(a[i],i+1)
        b.append(a[i]**(i+1))
    if sum(b)==number:
        return "Disarium !!"
    return "Not !!"
