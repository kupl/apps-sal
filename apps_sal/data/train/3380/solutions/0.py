from re import sub

def look_and_say_sequence(s, n):
    for _ in range(1, n):
        s = sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
