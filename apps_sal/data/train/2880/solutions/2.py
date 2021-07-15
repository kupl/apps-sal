seven = lambda m,s=0: (m,s) if m<100 else seven(m//10-2*(m%10), s+1)
