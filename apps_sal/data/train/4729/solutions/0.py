digits = 'zero one two three four five six seven eight nine'.split()

def f(n):
    return ''.join(map(digits.__getitem__, map(int, str(n))))

def numbers_of_letters(n):
    result = [f(n)]
    print(n, result)
    while result[-1] != 'four':
        result.append(f(len(result[-1])))
    return result
