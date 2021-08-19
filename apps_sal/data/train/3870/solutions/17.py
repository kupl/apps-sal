def solve(s):
    s_list = s.split(' ')
    s_nospace = ''
    for i in s_list:
        s_nospace += i
    s_nospace_reverse = ''
    for i in range(1, len(s_nospace) + 1):
        s_nospace_reverse += s_nospace[-i]
    final_s = ''
    space_index = []
    for i in range(0, len(s)):
        if s[i] == ' ':
            space_index.append(i)
    sdvig = 0
    for i in range(0, len(s_nospace)):
        if i + sdvig in space_index:
            final_s += ' '
            sdvig += 1
        if i < len(s_nospace):
            final_s += s_nospace_reverse[i]
    if s[-1] == ' ':
        final_s += ' '
    return final_s
