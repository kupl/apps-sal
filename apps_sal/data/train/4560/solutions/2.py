def answer(question, informations):
    question_words = set(question.lower().split())

    def compare(information):
        return len(question_words & set(information.lower().split()))
    return max([''] + informations, key=compare) or None
