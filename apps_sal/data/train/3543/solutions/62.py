def increment_string(strng):
    if len(strng) == 0:
        return '1'
    if not strng[-1].isdigit():
        return strng + '1'
    elif len(strng) == 1:
        return str(int(strng) + 1)
    idx = 0
    for (i, c) in enumerate(strng):
        if not c.isdigit():
            idx = i
    num_str = strng[idx + 1:]
    inc_num_str = str(int(num_str) + 1)
    return strng[:idx + 1] + inc_num_str.zfill(len(num_str))
    'if len(strng) > 0 and strng[-1].isdigit():\n        next_num = int(strng[-1]) + 1\n    \n        cur_index = -1 # Start at end of string\n        \n        if next_num < 10:\n            strng = strng[:cur_index] + str(next_num)\n        else:\n            strng = strng[:cur_index] + str(0)\n            cur_index -= 1\n            \n            while (abs(cur_index) <= len(strng)):\n                if not strng[cur_index].isdigit():\n                    return strng[:cur_index ] + "1" + strng[cur_index:]\n                \n                cur_num = int(strng[cur_index])\n                if cur_num < 9:\n                    strng = strng[:cur_index] + str(cur_num + 1) + strng[cur_index + 1:]\n                    return strng\n                else:\n                    strng = strng[:cur_index] + str(0) + strng[cur_index + 1:]\n                    cur_index -= 1\n    else:\n        strng += \'1\'\n                \n    return strng\n    '
