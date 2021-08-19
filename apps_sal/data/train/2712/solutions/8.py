def calculate_loneliness(s, ind):
    rng = int(s[ind])
    if ind - rng < 0:
        res_str = s[:ind] + s[ind + 1:ind + rng + 1]
        return sum([int(char) for char in res_str])
    res_str = s[ind - rng:ind] + s[ind + 1:ind + rng + 1]
    return sum([int(char) for char in res_str])


def loneliest(n):
    s = str(n)
    if '1' not in s:
        return False
    lone_list = []
    lst = []
    for i in range(len(s)):
        lone_list.append(calculate_loneliness(s, i))
        lst.append(int(s[i]))
    min_1 = lone_list[s.find('1')]
    for i in range(len(lone_list)):
        if lst[i] == 1:
            if lone_list[i] < min_1:
                min_1 = lone_list[i]
    if min(lone_list) == min_1:
        return True
    return False
