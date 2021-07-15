def row_weights(array):
    sum1=sum(array[i] for i in range(0,len(array),2))
    return (sum1,sum(array)-sum1)
