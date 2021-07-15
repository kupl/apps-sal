def sort_it(s, n):
   return ', '.join(sorted(s.split(', '), key=lambda s: s[n-1]))
        

