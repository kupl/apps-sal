def reverse_and_combine_text(s):
    if ' ' not in s:
        return s
    li = [i[::-1] for i in s.split()]
    return reverse_and_combine_text(' '.join((''.join(li[i:i + 2]) for i in range(0, len(li), 2))))
