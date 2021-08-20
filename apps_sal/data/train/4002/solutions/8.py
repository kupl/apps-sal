import re
PATTERNS = (('Roma', '.*?'.join('bug')), ('Maxim', '.*?'.join('boom')), ('Danik', '.*?'.join('edits')))


def memesorting(meme):
    result = (float('inf'), 'Vlad')
    for (name, p) in PATTERNS:
        res = re.search(p, meme, re.IGNORECASE)
        if res:
            result = min(result, (res.span()[1], name))
    return result[1]
