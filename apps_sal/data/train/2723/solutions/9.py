def average_string(s):
    n = 0
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] in dic:
            n += dic[s[i]]
        else:
            return 'n/a'
    n //= len(s)
    for key in dic:
        if dic.get(key) == n:
            n = key
    return n
