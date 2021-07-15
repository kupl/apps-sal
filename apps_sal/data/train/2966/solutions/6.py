from operator import add, sub


def calculate(s):
    nums = []
    op = None
    for word in s.split():
        if word.isdigit():
            nums.append(int(word))
        elif word in ('gains', 'loses'):
            op = add if word == 'gains' else sub
    return op(*nums)

