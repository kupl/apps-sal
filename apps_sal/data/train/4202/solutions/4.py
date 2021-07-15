import itertools

def ulam_sequence(u0, u1, n):
    arr=[u0,u1]
    temp=u0+u1
    control=list(map(sum, list(itertools.combinations(arr,2))))
    while(len(arr)!=n):
        if(control.count(temp)==1):
            arr.append(temp)
            control=list(map(sum, list(itertools.combinations(arr,2))))
        temp+=1
    return arr
