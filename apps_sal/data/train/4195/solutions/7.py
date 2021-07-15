def merge(line):
    a,li,i= list(filter(lambda x:bool(x),line)),[],0
    while i < len(a):
        if i < len(a)-1 and a[i]==a[i+1] : a[i]+= a[i+1] ; li.append(a[i]) ; i+=1
        else : li.append(a[i])
        i+=1
    return li+[0]*(len(line)-len(li))
