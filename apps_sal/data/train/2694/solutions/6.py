points = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}

def paul(x):
    score = sum(map(points.get, x))
    return (
        'Super happy!' if score < 40 else
        'Happy!' if score < 70 else
        'Sad!' if score < 100 else
        'Miserable!'
    )
