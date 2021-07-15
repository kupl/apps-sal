def find_needed_guards(k):
    if len(k)%2==0:k.append(True)
    a=0
    for x in range(1,len(k),2):
        if k[x-1]==k[x+1]==True or k[x]==True:continue
        elif k[x-1]==True:
            k[x+1]=True
            a+=1
        else:a+=1
    return a
