def average_string(s):
    # your code here
    res = 0
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    str = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    for i in range(0, 10):
        num[i] = s.count(str[i])
    if sum(num) == 0 or sum(num) != s.count(' ') + 1:
        return "n/a"
    for i, val in enumerate(num):
        res += val * i
    res /= sum(num)
    if res > 9:
        return"n/a"

    return str[int(res)]
