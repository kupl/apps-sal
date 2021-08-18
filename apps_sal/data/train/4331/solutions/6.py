def heavy_metal_umlauts(boring_text):
    d = {'A': 'Ä', 'O': 'Ö', 'a': 'ä', 'E': 'Ë',
         'U': 'Ü', 'e': 'ë', 'u': 'ü', 'I': 'Ï',
         'Y': 'Ÿ', 'i': 'ï', 'y': 'ÿ', 'o': 'ö'}
    return ''.join(i if i not in d else d[i] for i in boring_text)
