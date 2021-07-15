animals = lambda h, l: (lambda c=(l-h*2)/2: (lambda ch=h-c: (ch, c) if (abs(ch)+int(abs(c)))==h else "No solutions")() )()
