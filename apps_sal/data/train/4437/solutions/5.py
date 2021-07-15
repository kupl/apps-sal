def cookie(x):
    return 'Who ate the last cookie? It was %s!' % ('the dog', 'Monica', 'Zach')[
                                (type(x) in (int, float)) + 2 * (type(x) == str)]
