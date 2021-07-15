d = [("H",50),("Q",25),("D",10),("N",5),("P",1)]
make_change=lambda m,i=0,cng=[]:make_change(*([m%d[i][1],i+1,cng+[(d[i][0],m//d[i][1])]] if m>=d[i][1] else [m,i+1,cng])) if m else dict(cng)

'''cng = {}
for i,j in d.items():
        if money>=j:
            cng[i] = money//j
            money %= j
return cng'''
