def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    n = str(num)
    l = len(n)
    result = {int(n[i:j]) for i in range(l-1) for j in range(i+2, l+1) if int(n[i]) and n[i:j] == n[i:j][::-1]}
    return sorted(result) if result else "No palindromes found"

