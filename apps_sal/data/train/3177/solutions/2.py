def is_pal(s):
    h = len(s) // 2
    return all(a == b for a, b in zip(s[:h], s[::-1][:h]))

def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    s = str(num)
    pals = set()
    for i, ch in enumerate(s):
        if ch == '0':
            continue
        for j in range(i + 2, len(s) + 1):
            test = s[i:j]
            if is_pal(test):
                pals.add(test)
    return sorted(int(x) for x in pals) or 'No palindromes found'

