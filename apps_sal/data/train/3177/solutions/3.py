from itertools import combinations_with_replacement as combs

def palindrome(num):
    is_palindrome = lambda chunk: chunk == chunk[::-1] and len(chunk) > 1 and not (chunk.startswith('0') or chunk.endswith('0'))
    s, l = str(num), len(str(num))
    if isinstance(num, int) and num > 0:
        lst = list(set(int(s[i:j]) for i,j in combs(range(l+1), 2) if is_palindrome(s[i:j])))
    else: 
        return 'Not valid'
    return sorted(lst) if len(lst) else 'No palindromes found'
