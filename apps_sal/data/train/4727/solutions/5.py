def remove_vowels(strng):
    str = ['a', 'i', 'u', 'e', 'o']
    for i in str:
        strng = strng.replace(i, '')
    return strng
