def char_freq(message):
    solution = {}
    for c in message:
        if c in solution:
            solution[c] += 1
            continue
        solution[c] = 1
    return solution
