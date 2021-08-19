def encode(string):
    from itertools import groupby
    encode_group = '{group_length}{char}'.format
    return ''.join([encode_group(group_length=len(tuple(group)), char=char) for (char, group) in groupby(string)])


def decode(string):
    import re
    encoded_group = re.compile('(?P<group_length>\\d+)(?P<char>[A-Z])')
    return re.sub(pattern=encoded_group, repl=lambda match: int(match.group('group_length')) * match.group('char'), string=string)
