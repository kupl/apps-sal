from functools import partial

def score(q, a):
    return len(q.intersection(a.lower().split()))

def answer(question, information):
    q = set(question.lower().split())
    a = max(information,key=partial(score, q))
    if score(q, a):
        return a
