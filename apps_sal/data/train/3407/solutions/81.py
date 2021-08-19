def IsPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def palindrome_chain_length(n):
    result = 0
    while not IsPalindrome(n):
        n = n + int(str(n)[::-1])
        result += 1
    return result
