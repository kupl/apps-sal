def solve(s):
    nums = 0
    for char in s:
        if char.isdigit():
            pass
        else:
            s = s.replace(char,' ')
    result_list = s.split()
    for i in range(len(result_list)):
        result_list[i] = int(result_list[i])
    return (max(result_list))
