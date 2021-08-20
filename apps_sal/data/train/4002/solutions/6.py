def memesorting(meme):
    (bug, boom, edits) = (['b', 'u', 'g'], ['b', 'o', 'o', 'm'], ['e', 'd', 'i', 't', 's'])
    for ch in meme.lower():
        if ch == bug[0]:
            bug.pop(0)
            if not bug:
                return 'Roma'
        if ch == boom[0]:
            boom.pop(0)
            if not boom:
                return 'Maxim'
        if ch == edits[0]:
            edits.pop(0)
            if not edits:
                return 'Danik'
    return 'Vlad'
