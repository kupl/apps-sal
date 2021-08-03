def sillycase(silly):
    output = ''
    for c in range(len(silly)):
        if c < len(silly) / 2:
            output += str.lower(silly[c])
        else:
            output += str.upper(silly[c])
    return output
