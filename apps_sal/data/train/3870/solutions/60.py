def solve(s):
    space_indexes = [i for (i, c) in enumerate(s) if c == ' ']
    no_spaces_reversed = list(reversed([c for c in s if c != ' ']))
    for index in space_indexes:
        no_spaces_reversed.insert(index, ' ')
    return ''.join(no_spaces_reversed)
