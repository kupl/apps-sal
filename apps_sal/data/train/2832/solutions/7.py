def array_equalization(a, k):
    l_a=len(a)
    if k>=l_a-1:
        return 1
    sa=set(a)
    times_list=[]
    for i in sa:
        templs=[]
        times = 0
        for j in range(0,l_a):
            if (j>0 and j ==len(templs)) or j==0 :
                if a[j] == i:
                    templs.append(i)
                else:
                    templs+=[i]*k
                    times+=1
        times_list.append([times])
    return min(times_list)[0]
