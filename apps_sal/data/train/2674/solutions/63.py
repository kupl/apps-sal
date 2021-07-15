def two_sort(array):
    '''
    first we sort the array by sort() function :->
    and then we will take its first element and use it to get output :->
    '''
    array.sort()
    return ''.join([i+'***' for i in array[0]])[:-3]


