def answer(question, information):
    words = set([w for w in question.lower().split()])
    r = sorted([(len(set([w for w in info.lower().split()]) & words), info) for info in information])[-1]
    return r[1] if r[0] else None
