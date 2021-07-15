def square_array(arr):
    return [item**2 for item in arr]

def cube_array(arr):
    return [item**3 for item in arr]

def sum_array(arr):
    sum = 0
    for thing in arr:
        sum += thing
    return sum

def array_madness(a,b):
    return sum_array(square_array(a)) > sum_array(cube_array(b))
    

