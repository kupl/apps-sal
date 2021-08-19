def make_upper_case(s):
    alphabet = {}
    counter = 65
    for i in range(97, 123):
        alphabet[chr(i)] = chr(counter)
        counter = counter + 1
    sum = ''
    for i in s:
        for j in alphabet:
            if i == j:
                sum = sum + alphabet[j]
                i = ''
                break
        sum = sum + i
    return sum
