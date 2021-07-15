def getVolumeOfCubiod(length, width, height):
    result = (float(length) * float(width) * float(height))
    if float.is_integer(result) is True:  # Checking to see if I can convert the return a int
        return int(result)  # Returning int becuase it is possible
    else:
        return result  # Returning a float because the value isn't a whole number


