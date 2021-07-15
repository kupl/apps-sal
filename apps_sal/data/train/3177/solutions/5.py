def palindrome(num):
    if not (isinstance(num, int) and num > 0):
        return 'Not valid'
    s = str(num)
    result = set()
    for i in range(0, len(s)-1):
        for j in range(i+2, len(s)+1):
            if s[i] == '0':
                continue
            x = s[i:j]
            if x == x[::-1]:
                result.add(int(x))
    if result:
        return sorted(result)
    return 'No palindromes found'
