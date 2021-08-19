def answer(information, question):
    i = set(map(str.lower, information.split()))
    m = max([''] + question, key=lambda x: sum((x.lower() in i for x in x.split())))
    return m or None
