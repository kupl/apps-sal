def vector_length(vector):
    return sum(((a - b) ** 2 for (a, b) in zip(*vector))) ** 0.5
