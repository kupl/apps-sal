def flatten_me(nput):
    output = []
    for itm in nput:
        if isinstance(itm, list):
            output += flatten_me(itm)
        else:
            output += [itm]
    return output
