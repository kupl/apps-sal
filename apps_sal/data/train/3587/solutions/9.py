def original_number(s):

    s = list(s)
    output = []
    nums = (('Z', 'ZERO', '0'),
            ('W', 'TWO', '2'),
            ('U', 'FOUR', '4'),
            ('X', 'SIX', '6'),
            ('G', 'EIGHT', '8'),
            ('O', 'ONE', '1'),
            ('H', 'THREE', '3'),
            ('F', 'FIVE', '5'),
            ('V', 'SEVEN', '7'),
            ('I', 'NINE', '9'))

    for n in nums:
        while n[0] in s:
            output.append(n[2])
            for c in n[1]:
                del s[s.index(c)]

    return ''.join(sorted(output))
