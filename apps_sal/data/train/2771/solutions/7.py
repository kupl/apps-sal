hofstadter_Q_values = [0, 1, 1]

def hofstadter_Q(n):
    values = hofstadter_Q_values
    for i in range(len(values), n + 1):
        values.append(
            values[i - values[i - 1]] +
            values[i - values[i - 2]])
    return values[n]
