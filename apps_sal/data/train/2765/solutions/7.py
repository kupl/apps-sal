def compare(a, b):
    return max((b, a), key=lambda sel:
        (sel.count('#'), sel.count('.'),
            sum(not t.startswith(('.', '#', '*')) for t in sel.split())))
