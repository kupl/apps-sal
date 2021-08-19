trans = dict(zip('6174329805', 'abdeilmnot'))


def hidden(num):
    return ''.join((trans[char] for char in str(num)))
