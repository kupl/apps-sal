def remove_vowels(strng):
    gl = 'aoeiu'
    return ''.join([c for c in strng if c not in gl])
