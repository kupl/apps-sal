import re


def spreadsheet(s):
    nums = re.findall('(\\d+)', s)
    if len(nums) == 2:
        (n, cStr) = (int(nums[1]), '')
        while n:
            (n, r) = divmod(n - 1, 26)
            cStr += chr(r + 65)
        return '{}{}'.format(cStr[::-1], nums[0])
    else:
        return 'R{}C{}'.format(nums[0], sum((26 ** i * (ord(c) - 64) for (i, c) in enumerate(re.sub('\\d', '', s)[::-1]))))
