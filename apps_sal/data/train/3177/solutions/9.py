def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    check = str(num)
    total = set()
    for i in range(2, len(check) + 1):
        for j in range(len(check) - i + 1):
            if check[j:j + i][0] == "0" or check[j:j + i][-1] == "0":
                continue
            if is_palin(check[j:j + i]):
                total.add(int(check[j:j + i]))
    return sorted(total) if total else "No palindromes found"


def is_palin(s):
    return s[::-1] == s
