def unlock(message):
    a = {'abc': 2, 'def': 3, 'ghi': 4, 'jkl': 5, 'mno': 6, 'pqrs': 7, 'tuv': 8, 'wxyz': 9}
    return ''.join((str(a[y]) for x in message.lower() for y in a.keys() if x in y))
