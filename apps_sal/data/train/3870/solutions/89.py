def solve(s):
    index_list = [i for i in range(len(s)) if s.startswith(' ', i)]

    s = s.replace(' ', '')

    reversed_string = [s[-x] for x in range(1, len(s) + 1, 1)]

    for value in index_list:
        reversed_string.insert(value, ' ')

    return ''.join(reversed_string)
