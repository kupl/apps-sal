def well(x):
    cnt = 0
    for idea in x:
        cnt += 1 if idea == 'good' else 0
    return 'Fail!' if cnt == 0 else 'Publish!' if cnt <=2 else 'I smell a series!'
