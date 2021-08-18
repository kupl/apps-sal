import re


def to_chinese_numeral(n):
    numerals = {
        "-": "负",
        ".": "点",
        0: "零",
        1: "一",
        2: "二",
        3: "三",
        4: "四",
        5: "五",
        6: "六",
        7: "七",
        8: "八",
        9: "九",
        10: "十",
        100: "百",
        1000: "千",
        10000: "万"
    }

    plus_minus, num_part, dec_part = re.search(r'^(-)?(\d+)(?:\.(\d+))?$', str(round(n, 8))).groups()

    plus_minus = numerals['-'] if plus_minus else ''

    num_len = len(num_part)
    num_chinese = ''

    if num_len == 1:
        num_chinese = numerals[int(num_part)]
    else:
        num_rev = num_part[::-1]

        for i in range(num_len - 1, -1, -1):
            digit_value = int(num_rev[i])
            digit_value_chinese = numerals[digit_value]
            place_multi_chinese = numerals[int(10 ** i)]

            if i == 1:
                if num_len > 2:
                    if digit_value > 0:
                        num_chinese += digit_value_chinese + place_multi_chinese
                        if num_rev[i - 1] == '0':
                            break
                    else:
                        if sum(int(num_rev[j]) for j in range(i, -1, -1)) > 0:
                            num_chinese += numerals[0]
                else:
                    if digit_value == 1:
                        num_chinese += place_multi_chinese
                        if num_rev[i - 1] == '0':
                            break
                    else:
                        num_chinese += digit_value_chinese + place_multi_chinese
                        if num_rev[i - 1] == '0':
                            break
            else:
                if digit_value > 0:
                    if digit_value != 0:
                        num_chinese += digit_value_chinese
                        if i > 0:
                            num_chinese += place_multi_chinese
                else:
                    if sum(int(num_rev[j]) for j in range(i)) > 0 and num_rev[i - 1] != '0':
                        num_chinese += numerals[0]

    if dec_part:
        dec_len = len(dec_part)
        dec_chinese = numerals['.']
        for i in range(dec_len):
            dec_chinese += numerals[int(dec_part[i])]
    else:
        dec_chinese = ''

    return '{}{}{}'.format(plus_minus, num_chinese, dec_chinese)
