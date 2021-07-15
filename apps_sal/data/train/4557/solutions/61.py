def row_weights(array):
    s1,s2=0,0
    for i in range(0,len(array)):
        if (i+1)%2==1:
            s1+=array[i]
        else:
            s2+=array[i]
            
    return (s1,s2)
