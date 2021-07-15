sel_number = lambda n, d:len([x for x in range(10,n+1) if sorted(list(set(list(str(x)))))==list(str(x)) and all((int(str(x)[i])-int(str(x)[i-1]))<=d for i in range(1,len(str(x))))])
