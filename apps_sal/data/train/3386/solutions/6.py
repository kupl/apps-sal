alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_column_title(number):
    result = []
    if not isinstance(number, int):
        raise TypeError

    def convert(num):
        if isinstance(num, list):
            n = num[0]
        else:
            if len(result) == 0:
                result.append(num)
            n = num
        if 0 < n <= 26:
            result.append(alphabet[n - 1])
            return result
        else:
            if n % 26 == 0:
                result[0] = convert(n // 26 - 1)
            else:
                result[0] = convert(n // 26)
            result.append(alphabet[n % 26 - 1])
            return result
    res = convert(number)
    result = []
    return ''.join(res[1:])
