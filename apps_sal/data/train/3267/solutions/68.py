def well(x):
    if x.count('good') == 0: return "Fail!"
    return 'Publish!' if x.count('good') == 1 or x.count('good') == 2 else "I smell a series!"
