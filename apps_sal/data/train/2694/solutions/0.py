def paul(x):
    points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    misery = sum(map(points.get, x))
    return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!']\
            [(misery<40)+(misery<70)+(misery<100)]
