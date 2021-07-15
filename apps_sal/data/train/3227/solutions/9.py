love = str.maketrans("abcdefghijklmnopqrstuvwxyz", 'LOVELOVELOVELOVELOVELOVELO')

def to_lover_case(string):
    return string.lower().translate(love)
