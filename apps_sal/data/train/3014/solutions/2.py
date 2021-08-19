def simple_transposition(text):
    rowOne = True
    one = ''
    two = ''
    for x in text:
        if rowOne:
            one += x
        else:
            two += x
        rowOne = not rowOne
    return str(one) + str(two)
