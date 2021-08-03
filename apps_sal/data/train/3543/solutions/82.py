def increment_string(strng):
    end_num_str = ''
    while strng[-1:].isnumeric():
        end_num_str = strng[-1:] + end_num_str
        strng = strng[:-1]
    num_len = len(end_num_str)
    end_num_str = str(int(end_num_str) + 1) if end_num_str else '1'
    while len(end_num_str) < num_len:
        end_num_str = '0' + end_num_str
    return strng + end_num_str
