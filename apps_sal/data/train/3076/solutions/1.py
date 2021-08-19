def solve(arr):
    (go_moves, go_places) = list(zip(*(s.split(' ', 1) for s in arr)))
    back_moves = ['Begin'] + ['Right' if s == 'Left' else 'Left' for s in go_moves[:0:-1]]
    return [' '.join(z) for z in zip(back_moves, go_places[::-1])]
