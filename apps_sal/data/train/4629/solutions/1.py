# return str of the smallest value of the combined numbers in a_list
def penalty(a_list):
    return ''.join(sorted(a_list, key=lambda n: n + n[:1]))
