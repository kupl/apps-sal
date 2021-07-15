
def capitalize(s,ind):
    return  "".join((list([i[1].upper() if i[0] in ind else i[1] for i in enumerate(s)])))

