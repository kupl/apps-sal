def sum_array(arr):
    if(arr == None):
        return 0
    else:
        list.sort(arr)
        sum = 0
        length = len(arr)
        if 1 >= length:
            return sum
        else:
            array = arr
            array = array[1:len(array)-1]
            for x in array:
                sum += x
            return sum
        
        

