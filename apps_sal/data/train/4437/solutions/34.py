def cookie(x):
    ergebnis = ''

    if type(x) == str:
        ergebnis = "Who ate the last cookie? It was Zach!"
    elif type(x) in (int, float):
        ergebnis = "Who ate the last cookie? It was Monica!"
    else:
        ergebnis = "Who ate the last cookie? It was the dog!"

    return ergebnis
