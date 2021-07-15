def reverse_alternate(string):
    splitted = string.split()
    converted = []
    for elt in splitted :
        if splitted.index(elt) % 2 != 0 :
            reversed = ''.join(char for char in elt[::-1])
            converted.append(reversed)
        else :
            converted.append(elt)
    return ' '.join(converted)
