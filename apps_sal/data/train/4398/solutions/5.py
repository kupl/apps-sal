def elevator_distance(array):
    a=0
    for i in range(0, len(array)-1):
     a+=abs(int(array[i]) - int(array[i+1]))
    return a

