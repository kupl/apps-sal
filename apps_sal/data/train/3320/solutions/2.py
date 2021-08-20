nums = ['six', 'five', 'four', 'three', 'two', 'one']
lines = {'hhh': '----o----', 'hht': '---- ----', 'htt': '---------', 'ttt': '----x----'}


def oracle(arr):
    return '\n'.join((lines[''.join(sorted(l[1:]))] for l in sorted(arr, key=lambda l: nums.index(l[0]))))
