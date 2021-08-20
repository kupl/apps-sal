def two_sort(array):
    result = ''
    word = sorted(array)[0]
    n = 0
    while n < len(word):
        if len(word) - n == 1:
            result += word[n]
        else:
            result += word[n] + '***'
        n += 1
    return result
