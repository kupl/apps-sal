def solve(directions):
    positions, turns = [], []
    for d in directions[::-1]:
        t, p = d.split(' on ')
        turns.append('Right' if t == 'Left' else 'Left')
        positions.append(p)
    result = [f'{t} on {p}' for t, p in zip(turns, positions[1:])]
    return [f'Begin on {positions[0]}'] + result
