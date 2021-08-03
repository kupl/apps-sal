def palindrome(n):
    if type(n) != int or n < 0:
        return 'Not valid'
    n, p = str(n), set()
    for i in range(len(n)):
        for j in range(i + 2, len(n) + 1):
            sub = n[i:j]
            if sub == sub[::-1] and sub[0] != '0' != sub[-1]:
                p.add(sub)
    return sorted(map(int, p)) or 'No palindromes found'
