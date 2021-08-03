def palindrome_chain_length(n, c=0): return (lambda pal: c if n == pal else palindrome_chain_length(n + pal, c + 1))(int(str(n)[::-1]))
