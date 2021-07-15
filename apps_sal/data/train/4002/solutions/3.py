def memesorting(meme):
    keys = { 'bug':'', 'boom':'', 'edits':''}
    for i, l in enumerate(meme.lower()):
        for key, value in { 'bug':'Roma', 'boom':'Maxim', 'edits':'Danik' }.items():
            if l == key[len(keys[key])]:
                keys[key] += l
                if keys[key] == key:
                    return value
    return 'Vlad' 
