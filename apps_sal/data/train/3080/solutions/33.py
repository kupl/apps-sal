def who_is_paying(name):

    petition = []

    if len(name) <= 2:
        petition.append(name)
        return petition

    else:
        nam = name[:2]
        petition.append(name)
        petition.append(nam)
        return petition
