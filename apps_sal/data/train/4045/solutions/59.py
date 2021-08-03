def number(lines):
    numlist = []
    numb = 1
    for x in lines:
        numlist.append(str(numb) + ": " + x)
        numb += 1

    return numlist
