def increment_string(string):
    numbers = ''
    others = ''
    if string == '':
        return '1'
    for i in range(len(string) - 1, -1, -1):
        if '0' <= string[i] <= '9':
            numbers = string[i] + numbers
        if string[i] < '0' or string[i] > '9':
            others = string[:i + 1]
            break
    if numbers == '':
        return others + '1'
    i = 0
    while numbers[i] == '0' and i < len(numbers) - 1:
        i = i + 1
    zeros = ''
    if i != 0:
        zeros = numbers[:i]
        numbers = numbers[i:]
    if len(numbers) != len(str(int(numbers) + 1)) and zeros != '':
        zeros = zeros[:-1]
    numbers = str(int(numbers) + 1)
    return others + zeros + numbers
