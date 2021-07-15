def is_palindrome(str):
    str = f"{str}"
    x = str[::-1]
    temp = - ((len(str) - 1 ) // 2 + 1 )
    if str[:-temp] == x[:-temp]:
        return True
    return False
