def getVolumeOfCubiod(length, width, height):
    result = (float(length) * float(width) * float(height))
    if float.is_integer(result) is True:
        return int(result)
    else:
        return result
