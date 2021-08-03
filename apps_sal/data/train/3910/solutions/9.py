from itertools import chain, zip_longest


def operator_insertor(target):
    return min((x.count('+') + x.count('-') for x in insertions(target, [1, 2, 3, 4, 5, 6, 7, 8, 9])), default=None)


def insertions(rem, nums, ops=''):
    if len(nums) == 1:
        return ([''.join(map(''.join, zip_longest('123456789', ops, fillvalue=''))).replace('|', '')]
                if rem - nums[0] == 0 else [])
    return list(chain(insertions(rem - nums[0], nums[1:], ops + '+'),
                      insertions(rem - nums[0], [-nums[1]] + nums[2:], ops + '-'),
                      insertions(rem, [int(f'{nums[0]}{nums[1]}')] + nums[2:], ops + '|')))
