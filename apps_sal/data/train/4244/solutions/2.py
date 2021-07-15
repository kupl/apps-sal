palindrome=lambda n:[sum(str(n).count(i)&1 for i in set(str(n)))<2,0][n<10] if type(n)==int and n >= 0 else 'Not valid'
