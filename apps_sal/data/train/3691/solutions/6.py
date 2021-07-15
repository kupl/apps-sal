get_a_down_arrow_of=lambda n,m=lambda s:s+s[-2::-1]:'\n'.join(' '*i+m(('1234567890'*n)[:n-i])for i in range(n))
