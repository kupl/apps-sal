def greet(*s):
    return f"Hello {['boss', 'guest'][len(set(s)) == len(s)]}"
