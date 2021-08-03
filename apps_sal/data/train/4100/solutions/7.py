def reverse_alternate(string):
    return " ".join(j if i % 2 == 0 else j[::-1] for i, j in enumerate(string.split()))
