def answer(question, information):
    (score, info) = max(((sum((word in info.lower().split() for word in question.lower().split())), info) for info in information))
    return None if not score else info
