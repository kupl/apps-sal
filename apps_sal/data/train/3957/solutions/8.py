def uniq_c(seq): 
    seq.append('asdadasd')
    arr = []
    count = 1
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            count +=1
        else:
            arr.append((seq[i], count))
            count = 1
    return arr
