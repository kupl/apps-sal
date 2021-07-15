opposite = {
    'white': 'black',
    'black': 'white'
}

def whoseMove(last, win):
    return last if win else opposite[last]
