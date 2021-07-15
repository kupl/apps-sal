def count_correct_characters(c, g):
    if len(c) != len(g): raise Exception('Error')
    return sum(1 for i,j in zip(c,g) if i==j)
