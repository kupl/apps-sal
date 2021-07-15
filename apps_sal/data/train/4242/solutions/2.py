NEXT = {'R': 'D', 'D': 'L', 'L': 'U', 'U': 'R'}

def direction_in_grid(n, m, d='R'):
    while n > 1:
        n, m, d = m, n-1, NEXT[d]
    return d
