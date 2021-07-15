def number(lines):
    #your code here
    i=1
    l=[]
    for item in lines:
        l.append((str(i)+": "+item))     
        i+=1                              # for line counter
    return l
