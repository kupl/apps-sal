def cookie(x):
    pre = 'Who ate the last cookie? It was '
    post = 'the dog'
    punc = '!'
    if type(x) == str:
        post = "Zach"
    elif type(x) == int or type(x) == float:
        post = "Monica"
    return pre + post + punc
