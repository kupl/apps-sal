TRANS = dict(zip('abcdefghijklmnopqrstuvwxyz',
                 '22233344455566677778889999'))

def unlock(message):
    return ''.join( TRANS[c] for c in message.lower() )
