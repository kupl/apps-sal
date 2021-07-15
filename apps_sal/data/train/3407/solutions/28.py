def reverse_int(n: int) -> int:
    return int(str(n)[::-1])

def palindrome_chain_length(n: int, i: int = 0) -> int:
    return i if reverse_int(n) == n else palindrome_chain_length(n + reverse_int(n), i + 1)
