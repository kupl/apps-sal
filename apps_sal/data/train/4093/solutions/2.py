def find_a(array, n):
    if n > 3:
        for i in range(4,n+1):
            array.append(6*array[i-1]+6*array[i-3]-10*array[i-2]-array[i-4])
        return array[-1]
    elif n < 0:
        array = array[::-1]
        for i in range(4,4-n):
            array.append(6*array[i-1]+6*array[i-3]-10*array[i-2]-array[i-4])
        return array[-1]
    else:
        return array[n]
