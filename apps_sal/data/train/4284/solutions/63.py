def array_leaders(numbers):
    li=[]
    for s in range(len(numbers)*-1,0):
        if s==-1:
            if numbers[-1]>0:
                li.append(numbers[s])
            else:
                break
        elif sum(numbers[s+1:])<=numbers[s]:
            li.append(numbers[s])
        else:
            continue
    return li

