square_it=lambda n:len(str(n))**.5%1and"Not a perfect square!"or'\n'.join(map(''.join,zip(*[iter(str(n))]*int(len(str(n))**.5))))
