even_magic=lambda n:[[y%4in(x%4,3-x%4)and n*n-n*y-x or n*y+x+1for x in range(n)]for y in range(n)]
