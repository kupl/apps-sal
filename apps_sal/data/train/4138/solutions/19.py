def count_correct_characters(c, g):
    if len(c) != len(g): raise ValueError('Is this the error you wanted?')
    else: return sum([1 for i in zip(c,g) if i[0]==i[1]])

