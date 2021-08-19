def solve(s):
    rev = list(s.replace(' ', '')[::-1])
    for (index, item) in enumerate(s):
        if item == ' ':
            rev.insert(index, item)
    return ''.join(rev)
