def bin_str(s):
    count = 0
    while s.count('1') != 0:
        first_index = s.index('1')
        n = ''
        for nbr in s[first_index:len(s)]:
            if nbr == '1':
                n += '0'
            elif nbr == '0':
                n += '1'
        s = s[0:first_index] + n
        count += 1
    return count
