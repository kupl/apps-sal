def balanced_num(number):
    array = list(map(int, str(number)))
    if len(array) % 2 == 0:
        left_side = array[0:int(len(array)/2-1)]
        right_side = array[int(len(array)/2)+1:len(array)]
    else:
        left_side = array[0:int(len(array)/2)]
        right_side = array[int(len(array)/2)+1:len(array)]
    left_sum = 0
    right_sum = 0
    for i in left_side:
        left_sum += i
    for j in right_side:
        right_sum += j

    if left_sum != right_sum:
        return "Not Balanced" 
    else:
        return "Balanced" 
