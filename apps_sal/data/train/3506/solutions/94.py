def vowel_indices(word):
    retVal = []
    checkList = 'aeiouy'
    for (i, x) in enumerate(word.lower()):
        print(('Looking at ', x))
        try:
            l = checkList.index(x)
            retVal.append(i + 1)
            print(('think this is a vowel', x))
        except ValueError:
            print(('discarded', x))
    return retVal
