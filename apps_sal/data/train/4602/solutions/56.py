def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    nT = len(test)
    nO = len(original)
    if nO == nT:
        counterT = [0] * (255 + 1)
        counterO = [0] * (255 + 1)
        for x in range(nT):
            counterT[ord(test[x])] += 1
            counterO[ord(original[x])] += 1
        if counterT == counterO:
            return True
        else:
            return False
    else:
        return False
