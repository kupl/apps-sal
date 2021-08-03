def pal(s): return all(a == b for a, b in zip(s[:len(s) // 2], s[::-1]))


def palindrome(num):
    if type(123) != type(num):
        return 'Not valid'
    n = str(num)
    if any(not c.isdigit() for c in n):
        return 'Not valid'
    R, l = [], len(n)
    for i in range(2, l + 1):
        for j in range(l - i + 1):
            t = n[j:j + i]
            if pal(t) and t[0] != '0':
                R.append(int(t))
    return sorted(set(R)) if R else 'No palindromes found'
