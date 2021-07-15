def divide(weight):
    return len([i for i in range(1, weight + 1) if i % 2 == 0]) >= 2 and weight % 2 == 0
