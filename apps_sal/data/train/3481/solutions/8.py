from collections import Counter

def get_char_count(stg):
    result = {}
    for char, count in Counter(sorted(c for c in stg.lower() if c.isalnum())).items():
        result.setdefault(count, []).append(char)
    return result
