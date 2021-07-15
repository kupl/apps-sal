def make_acronym(phrase):
    if not isinstance(phrase, str): return 'Not a string'
    arr = phrase.split()
    return ''.join(a[0] for a in arr).upper() if all(map(str.isalpha, arr)) else 'Not letters'       
