CLUSTERS = {
    'A': 'Left',
    'B': 'Left',
    'C': 'Left',
    'D': 'Middle',
    'E': 'Middle',
    'F': 'Middle',
    'G': 'Right',
    'H': 'Right',
    'K': 'Right',
}


def plane_seat(a):
    row = int(a[:-1])
    col = a[-1:]
    section = (
        'Front' if row <= 20 else
        'Middle' if row <= 40 else
        'Back' if row <= 60 else
        ''
    )
    cluster = CLUSTERS.get(col)
    if section and cluster:
        return f'{section}-{cluster}'
    else:
        return 'No Seat!!'
