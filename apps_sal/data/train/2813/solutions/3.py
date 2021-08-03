from string import ascii_lowercase as abc

ch = abc[::-1] + '!? '


def switcher(arr):
    return "".join(ch[int(x) - 1] if x != '0' else '' for x in arr)
