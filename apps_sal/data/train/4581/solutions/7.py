def are_similar(a, b):
    unmatch = list(filter(lambda x: x[0] != x[1], zip(a, b)))
    if len(unmatch) != 2:
        return unmatch == []
    return unmatch[0][::-1] == unmatch[1]
