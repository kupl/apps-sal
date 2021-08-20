def split_in_parts(s, part_length):
    newS = ''
    for i in range(len(s)):
        newS += f' {s[i]}' if i != 0 and i % part_length == 0 else s[i]
    return newS
