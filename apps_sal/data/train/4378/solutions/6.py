def find_spaceship(m):
    return 'Spaceship lost forever.' * ('X' not in m) or (lambda x=m.find('X'): [x - 1 - m[:x].rfind('\n'), m[x:].count('\n')])()
