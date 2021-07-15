def maketrans(n, a, b, c):
  if n == 0: return []
  return maketrans(n-1, a, c, b) + [[a, b]] + maketrans(n - 1, c, b, a)


def hanoiArray(n):
    transitions = maketrans(n, 0, 2, 1)
    state = [[i for i in range(n, 0, -1)], [], []]
    res = str(state)
    while transitions:
        from_peg, to_peg = transitions.pop(0)
        state[to_peg].append(state[from_peg].pop())
        res += '\n' + str(state)
    return res
