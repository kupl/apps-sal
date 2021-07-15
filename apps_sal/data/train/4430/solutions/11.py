def vowel_2_index(string):
    return ''.join( [str(i+1) if string[i].lower() in "aeiou" else string[i] for i in range(len(string))])
