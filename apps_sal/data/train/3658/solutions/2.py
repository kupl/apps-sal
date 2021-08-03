def swap(s, n):
    n = str(bin(n))[2:]
    index = 0
    new_s = ''
    for letter in s:
        if letter.isalpha():
            if n[index % len(n)] == '1':
                new_s += letter.swapcase()
            else:
                new_s += letter
            index += 1
        else:
            new_s += letter
    return new_s
