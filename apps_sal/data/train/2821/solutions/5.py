def trim(beard):
    return [list(map(lambda x:x.replace("J", "|"), arr)) for arr in beard[:-1]] + [["..."] * len(beard[0])]
