import math

# The function that will check a prefix and a suffix
def prefix_suffix_check(string, indexIn):
    return string[:indexIn] == string[(indexIn) * -1 : ]

def solve(initial_string):
    
    # Halves and floors the array size
    half_array_size = int(math.floor(len(initial_string) / 2))
    
    # A revese for loop for checking the middle to outer
    for x in range(half_array_size, 0, -1):
        # If the suffix and prefix are equal return the x
        if (prefix_suffix_check(initial_string, x) == True):
            return x
    
    # Else return 0
    return 0

