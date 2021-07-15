m = {
    'C': 'clubs',
    'D': 'diamonds',
    'H': 'hearts',
    'S': 'spades'
}
def define_suit(card):
    return m.get(card[-1])
