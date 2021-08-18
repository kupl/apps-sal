def penalty(a_list):
    return ''.join(sorted(a_list, key=lambda n: n + n[:1]))
