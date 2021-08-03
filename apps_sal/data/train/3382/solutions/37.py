def lowercase_count(strng):
    somme = 0
    for minuscule in strng:
        if(minuscule.islower()):
            somme += 1
    return somme
