from collections import Counter

def string_letter_count(s):
    cnt = Counter(filter(str.isalpha, s.lower()))
    return ''.join(f'{v}{k}' for k, v in sorted(cnt.items()))
