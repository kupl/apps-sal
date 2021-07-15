import re

empty = [''] * 6
separator = ['-'] * 6
bar = ['|'] * 6

def transpose(amount, tab):

    # "And if you listen very hard
    #  The tune will come to you at last..."

    #           -- Stairway to Heaven (1971)

    try:
        result = empty
        chunk = empty

        for i in range(len(tab[0])):
            column = get_column(tab, i)
            chunk = merge(chunk, column)
    
            if chunk == separator or chunk == bar:
                result = merge(result, chunk)
                chunk = empty
            elif column == separator:
                recalculated = recalculate(amount, chunk)
                result = merge(result, recalculated)
                chunk = empty

        return result
    except OutOfFretsException as oof:
        return str(oof)

def get_column(tab, column_idx):
    return [tab[string][column_idx] for string in range(0, 6)]

def merge(left, right):
    return [left[i] + right[i] for i in range(0, 6)]

def recalculate(amount, chunk):
    recalculated = [shift(string, amount) for string in chunk]
    max_length = max([len(s) for s in recalculated])
    padded = [string.ljust(max_length, '-') for string in recalculated]
    return shrink(padded)

def shrink(chunk):
    new_chunk = empty
    for i in range(len(chunk[0])):
        current_column = get_column(chunk, i)
        next_column = get_column(chunk, i + 1) if i + 1 < len(chunk[0]) else None

        if current_column == separator and next_column == separator:
            continue
        else:
            new_chunk = merge(new_chunk, current_column)

    return new_chunk

def shift(string, amount):
    tokens = re.findall(r'[^\d]*[0-9]+[^\d]*', string)
    if len(tokens) > 0:
        numbers = [int(re.findall(r'[0-9]+', t)[0]) for t in tokens]
        shifted = [(n, n + amount) for n in numbers]
        if (any(s[1] > 22 or s[1] < 0 for s in shifted)):
            raise OutOfFretsException()
        else:
            replaced = [tokens[i].replace(str(shifted[i][0]), str(shifted[i][1])) for i in range(len(tokens))]
            return "".join(replaced)
    else:
        return string

class OutOfFretsException(Exception):
    def __init__(self):
        Exception.__init__(self, 'Out of frets!')
