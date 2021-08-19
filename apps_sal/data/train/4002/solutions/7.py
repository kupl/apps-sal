def memesorting(meme):
    print(meme)
    targets = [['bug', 0, 'Roma'], ['boom', 0, 'Maxim'], ['edits', 0, 'Danik']]
    for char in meme:
        for target in targets:
            if char.lower() == target[0][target[1]]:
                target[1] += 1
                if target[1] == len(target[0]):
                    return target[2]
    return 'Vlad'
