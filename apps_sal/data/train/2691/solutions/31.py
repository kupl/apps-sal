def solve(s):
    s += 'a'
    digits = list('0123456789')
    biggest = 0
    current = ''
    list_of_numbers = []
    for i in range(len(s)):
        if s[i] in digits:
            current += s[i]
        else:
            list_of_numbers.append(current)
            current = ''

    while '' in list_of_numbers:
        list_of_numbers.remove('')
    list_of_ints = []
    for j in range(len(list_of_numbers)):
        list_of_numbers[j] = int(list_of_numbers[j])
        list_of_ints.append(list_of_numbers[j])
    biggest = max(list_of_ints)
    return biggest


pass
