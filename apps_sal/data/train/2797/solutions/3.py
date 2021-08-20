D = {}
for c in '0123456789*#':
    D[c] = 1
for c in 'adgjmptw':
    D[c] = 2
for c in 'behknqux':
    D[c] = 3
for c in 'cfilorvy':
    D[c] = 4
for c in 'sz':
    D[c] = 5


def mobile_keyboard(s):
    return sum(map(D.get, s))
