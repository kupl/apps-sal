def increment_string(st):
    if not st or st[-1].isalpha():
        return st + '1'
    if int(st[-1]) < 9:
        return st[:-1] + str(int(st[-1]) + 1)
    end, i = '', len(st) - 1
    while st[i].isdigit() and int(st[i]) == 9:
        i -= 1
        end += '0'
    return increment_string(st[:i + 1]) + end
