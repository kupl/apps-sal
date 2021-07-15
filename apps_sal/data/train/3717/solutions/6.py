def protects(location):
    """Returns the protected spaces (as a set), given a location.
       Examples:
          protects('b2') == {'a3', 'c3'}
          protects('a2') == {'b2'}
          protects('f8') == set()
    """
    if location[1] == '8':  return set()
    row = int(location[1]) + 1
    col = location[0]
    if col == 'a':
        cols = {'b'}
    elif col == 'h':
        cols = {'g'}
    else:
        cols = {chr(ord(col)-1), chr(ord(col)+1)}
    return {f'{c}{row}' for c in cols}


def covered_pawns(pawns):
    protected_spaces = set()
    for p in pawns:
        protected_spaces |= protects(p)
    return len(set(pawns) & protected_spaces)
