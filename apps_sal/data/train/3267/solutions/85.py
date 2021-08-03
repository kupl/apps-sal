def well(x):
    count = 0

    for idea in x:
        if idea == 'good':
            count += 1

    return 'Fail!' if count == 0 else 'Publish!' if count <= 2 else 'I smell a series!'
