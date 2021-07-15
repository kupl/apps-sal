# Return a new array consisting of elements 
# which are multiple of their own index in input array (length > 1).

# Some cases:

# [22, -6, 32, 82, 9, 25] =>  [-6, 32, 25]

# [68, -1, 1, -7, 10, 10] => [-1, 10]

def multiple_of_index(arr):
    b=[]
    for i in range(1, len(arr)):
        if arr[i]%i == 0:
            b.append(arr[i])
    return b
                   

