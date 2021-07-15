def two_sort(array):
    x=sorted(array)
    word=""
    for i in range(0,len(x[0])):
        word+=x[0][i]
        if i<len(x[0])-1: word+="***"
    return word
