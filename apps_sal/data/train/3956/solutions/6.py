def sort_string(s):
    return (lambda r: ''.join((r.pop(0) if e.isalpha() else e for e in s)))([e[0] for e in sorted(sorted([[k, i] for (i, k) in enumerate(s) if k.isalpha()], key=lambda a: a[1]), key=lambda a: a[0].lower())])
