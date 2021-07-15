palindrome_chain_length = lambda n: (lambda rev: 0 if n == rev(n) else palindrome_chain_length(n + rev(n)) + 1)(lambda n: int(''.join(list(reversed(str(n))))))


