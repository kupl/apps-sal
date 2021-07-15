palindrome_chain_length=lambda n,i=0:i if str(n)==str(n)[::-1] else palindrome_chain_length((n+int(str(n)[::-1])),i+1)
