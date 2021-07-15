from itertools import count

def count_deaf_rats(town):
    deaf = 0
    piper = False
    rat = ''
    for c in town:
        if c == 'P':
            piper = True
        if c in 'O~':
            rat += c
            if len(rat) == 2:
                deaf += piper != (rat == 'O~')
                rat = ''
    return deaf
