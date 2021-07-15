def gordon(a):
    return '!!!! '.join(a.upper().translate(str.maketrans('AEIOU', '@****')).split()) + '!!!!'
