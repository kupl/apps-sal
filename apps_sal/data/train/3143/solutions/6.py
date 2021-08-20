words = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety'
words = words.split(' ')


def num2word(n):
    if n < 20:
        return words[n]
    elif n < 100:
        return words[18 + n // 10] + ('' if n % 10 == 0 else '-' + words[n % 10])
    else:
        return num2word(n // 100) + ' hundred' + (' ' + num2word(n % 100) if n % 100 > 0 else '')


def sort_by_name(arr):
    return sorted(arr, key=num2word)
