frogify = lambda s, r=__import__('re').sub: r('\\w.*?(?=[.?!])', lambda m: ' '.join(m.group().split()[::-1]), ' '.join(r("[(),;'-]", '', s).split()))
