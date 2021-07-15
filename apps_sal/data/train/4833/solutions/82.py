def replace_exclamation(astr):
    vowels = 'aeiou'
    uppervowels = 'AEIOU'
    emptystring = ''
    for eachletter in astr:
        if eachletter in vowels or eachletter in uppervowels:
            emptystring = emptystring + '!'
        else:
            emptystring = emptystring + eachletter
    return emptystring

