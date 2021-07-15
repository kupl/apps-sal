def replace_exclamation(s):
    lijst = list(s)
    for i in range(0, len(lijst)):
        if lijst[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            lijst[i] = '!'
    return ''.join(lijst)
