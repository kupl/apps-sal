def gordon(a):
    return '!!!! '.join(a.upper().split()).translate(str.maketrans('AEIOU', '@****')) + '!!!!'
