def unite_unique(*arrays):
    output = []
    for arr in arrays:
        for i in arr:
            if i not in output:
                output.append(i)
    return output
