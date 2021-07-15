from itertools import cycle, islice

def vowel_shift(text, n):
    chrs = [c for c in text or '' if c.lower() in 'aeiou']
    if text and chrs:
        it = islice(cycle(chrs), -n % len(chrs), None)
        text = ''.join(next(it) if c.lower() in 'aeiou' else c for c in text)
    return text
