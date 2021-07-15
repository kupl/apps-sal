def reverse_alternate(string):
    return " ".join(y[::-1] if x%2 else y for x,y in enumerate(string.split()))
