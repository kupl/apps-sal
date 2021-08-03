def reverse_alternate(s):
    return ' '.join(w[::-1] if i % 2 else w for i, w in enumerate(s.split()))
