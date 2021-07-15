def memesorting(meme):
    bug = 'bug'
    boom = 'boom'
    edits = 'edits'
    for i in meme.lower():
        if i == bug[0]:
            bug = bug[1:]
            if len(bug) == 0:
                return "Roma"
        if i == boom[0]:
            boom = boom[1:]
            if len(boom)== 0:
                return "Maxim"
        if i == edits[0]:
            edits = edits[1:]
            if len(edits)== 0:
                return "Danik"
    return 'Vlad'
