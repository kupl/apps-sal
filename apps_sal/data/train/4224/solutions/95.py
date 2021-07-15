def dont_give_me_five(start,end):
    # your code here
    l=[]
    for i in range(start,end+1):
        if '5' not in str(i) :
            l.append(i)

 
    for j in l:
        if '5' in str(j):
            l.remove(j)
    print(l)
    return len(l)



                
                
            

