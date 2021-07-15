def twos_difference(lst): 
    lst1=[]
    for i in lst:
        for j in lst:
            if i-j==2 or i-j==-2:
                if (i,j) not in lst1 and (j,i) not in lst1:
                    if i<j:
                        lst1.append((i,j))
                    else:
                        lst1.append((j,i))
    lst1.sort()
    return lst1
