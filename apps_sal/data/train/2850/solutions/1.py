def gordon(s):
    return ' '.join((x + '!!!!' for x in s.upper().translate(str.maketrans('AIUEO', '@****')).split()))
