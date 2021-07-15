def answer(question, informations):
    question_words = set(question.lower().split())
    compare = lambda information: len(question_words & set(information.lower().split()))
    return max([""] + informations, key=compare) or None

