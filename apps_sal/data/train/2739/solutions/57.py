def cube_odd(arr):

    if any(str(char).isalpha() for char in arr) == True:
        return None

    return sum(char**3 for char in arr if char % 2 != 0)
