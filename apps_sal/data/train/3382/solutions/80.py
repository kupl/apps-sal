def lowercase_count(strng):
    results=0
    for letter in strng:
        if (letter.islower()):
            results=results+1
    return results
