def get_char(c):
    print(c)
    try:
        asciiDict = {i: chr(i) for i in range(256)}
        return asciiDict[c]
    except:
        return None
