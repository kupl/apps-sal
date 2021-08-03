def memesorting(meme):
    typ = ('Roma', 'Maxim', 'Danik')
    what = ('bug', 'boom', 'edits')

    bug_boom_edits = [list(l[::-1]) for l in what]
    for c in meme.lower():
        for i, l in enumerate(bug_boom_edits):
            if l[-1] == c:
                l.pop()
            if not l:
                return typ[i]
    else:
        return 'Vlad'
