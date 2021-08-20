def dollar_to_speech(value):
    if '-' in value:
        return 'No negative numbers are allowed!'
    vals = list(map(int, value.replace('$', '').split('.')))
    typs = ('dollar', 'cent')
    return (' and '.join(('{} {}'.format(v, t + 's' * (v != 1)) for (v, t) in zip(vals, typs) if v)) or '0 dollars') + '.'


DollarToSpeech = dollar_to_speech
