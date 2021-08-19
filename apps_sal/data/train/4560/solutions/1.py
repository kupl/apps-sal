import re


def answer(question, information):
    pattern = re.compile('\\b({})\\b'.format('|'.join(set(question.lower().split()))), re.I)
    m = max(((len(pattern.findall(i)), i) for i in information))
    return m[1] if m[0] else None
