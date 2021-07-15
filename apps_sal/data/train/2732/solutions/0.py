from collections import Counter

def blocks(s):
    sort = lambda c: (c.isdigit(), c.isupper(), c)
    answer, counter = [], Counter(s)
    while counter:
        block = ''.join(sorted(counter, key=sort))
        answer.append(block)
        counter = counter - Counter(block)
    return '-'.join(answer)
