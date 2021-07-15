def spacey(array):
    return ["".join(array[:i]) for i, _ in enumerate(array, 1)]
