def egged(year, span):
    if year==0: return "No chickens yet!"
    chickens=[]
    for y in range(year):
        for i in range(len(chickens)):
            chickens[i][1]+=1
            chickens[i][0]=int(0.8*chickens[i][0])
        chickens.append([300,0])
        chickens.append([300,0])
        chickens.append([300,0])
    return sum(i[0] for i in chickens if i[1]<span)
