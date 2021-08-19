def work_on_strings(a, b):

    # New A and B
    corA = ''
    corB = ''

    # Hash table
    lettersA = {}
    lettersB = {}
    for ia in a.lower():
        lettersA[ia] = a.lower().count(ia)

    for ib in b.lower():
        lettersB[ib] = b.lower().count(ib)

    # For A
    for let in a:
        if let in lettersB.keys() and lettersB[let] % 2 != 0:
            corA += let.swapcase()
        elif let.isupper() == True and let.lower() in lettersB.keys():
            if lettersB[let.lower()] % 2 != 0:
                corA += let.lower()
            elif lettersB[let.lower()] % 2 == 0:
                corA += let.upper()
        else:
            corA += let
    # For B
    for let in b:
        if let in lettersA.keys() and lettersA[let] % 2 != 0:
            corB += let.swapcase()
        elif let.isupper() == True and let.lower() in lettersA.keys():
            if lettersA[let.lower()] % 2 != 0:
                corB += let.lower()
            elif lettersA[let.lower()] % 2 == 0:
                corB += let.upper()
        else:
            corB += let

    return corA + corB
