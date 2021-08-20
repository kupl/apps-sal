def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    k = []
    s = str(num)
    for (i, x) in enumerate(s):
        string = [x]
        for j in s[i + 1:]:
            string.append(j)
            if string == string[::-1] and ''.join(string) not in k and (string[-1] != '0'):
                k.append(''.join(string))
    return k and sorted((int(x) for x in k)) or 'No palindromes found'
