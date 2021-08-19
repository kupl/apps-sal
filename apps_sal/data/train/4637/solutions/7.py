from math import ceil


def f(number, spoon):
    measure = 15 if spoon == 'tbsp' else 5
    grams = ceil(eval(f'{measure} * {number}'))
    return f'({grams}g)'


def convert_recipe(recipe):
    seq = recipe.split()
    res = []
    for (i, word) in enumerate(seq):
        res.append(word)
        if word in ('tbsp', 'tsp'):
            res.append(f(seq[i - 1], word))
    return ' '.join(res)
