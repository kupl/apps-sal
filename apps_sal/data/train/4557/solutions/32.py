def row_weights(array):
    x= sum(  [  array[i]   for i in range(len(array)) if i%2==1  ])
    y= sum(  [  array[i]   for i in range(len(array)) if i%2==0  ]) 
    return (y,x)
