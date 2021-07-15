def runoff(voters):
    if voters == []:
        return None
    elif len(voters[0]) == 1:
        return voters[0][0]
    voters_dict = {elem: [x[0] for x in voters].count(elem) for elem in voters[0]}
    expelled = sorted([voters_dict.get(x) for x in voters_dict])[0]
    return runoff([i for i in [[x for x in choices if
                                voters_dict.get(x) != expelled] for choices in voters] if i != []])
