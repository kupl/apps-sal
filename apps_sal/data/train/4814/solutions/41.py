def is_palindrome(s):
    List = list(s.lower())
    L = len(List)
    if L <= 1:
        return True
    if List[0] == List[L - 1]:
        del List[0]
        del List[L - 2]
        return is_palindrome(''.join(List))
    else:
        return False
