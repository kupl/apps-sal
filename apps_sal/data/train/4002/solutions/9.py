import regex as re
def memesorting(meme):
    meme = meme.lower()
    print(meme)
    check = []
    bug = re.search(r'b.*?u.*?g', meme)
    if bug is not None:
        check.append(bug)
    boom = re.search(r'b.*?o.*?o.*?m', meme)
    if boom is not None:
        check.append(boom)
    edits = re.search(r'e.*?d.*?i.*?t.*?s', meme)
    if edits is not None:
        check.append(edits)
    if check != []:
        first = min(check, key=lambda match: match.span()[1])
    else:
        return 'Vlad'
        
    if first.group()[-1] == 'g': return 'Roma'
    if first.group()[-1] == 's': return 'Danik'
    else: return 'Maxim'
    return
