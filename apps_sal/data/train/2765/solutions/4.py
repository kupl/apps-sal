def tokenise(s, split='*#. '):
    """
    Takes a string and splits it on any of the characters in the split string, 
    yields each split with the character used to split as it's prefix, with 
    the exception of spaces followed by another split character, when spaces 
    are removed

    Example:
        split('.abc #123 .def.ghi *')
    will yield the following strings:
        '.abc', '#123', '.def', '.ghi', '*'
    """
    buffer = ''
    for c in s:
        if c in split:
            if buffer.strip():
                yield buffer.strip()
                buffer = ''
        buffer += c
    if buffer.strip():
        yield buffer.strip()


def score_selector(selector):
    """
    Given a CSS selector build a score for the selector that can be used for 
    sorting precendence.

    Returns a tuple with counts of the following:
        (stars, ids, classes, tagnames)
    Stars are numbered positively, the others are numbered negatively 
    so that natural ordering can be used without having to specify a key
    for the sort call.
    """
    low, ids, classes, tags = 0, 0, 0, 0
    for part in tokenise(selector):
        if part.startswith('.'):
            classes -= 1
        elif part.startswith('#'):
            ids -= 1
        elif part.startswith('*'):
            low += 1
        else:
            tags -= 1

    return low, ids, classes, tags


def compare(a, b):
    """Compares two CSS selectors and returns the one with highest precedence"""
    return sorted([(score_selector(s), -i, s) for i, s in enumerate([a, b])])[0][-1]
