def to_alternating_case(string):
    NewString = []
    for stri in string:
        if type(stri) is str:
            NewString.append(stri.upper() if stri.islower() else stri.lower())
        else:
            NewString.append(stri)

    return (''.join(NewString))
