tr = lambda n: (n*(n+1))//2 if n>=0 else 0
shape_area = lambda n: tr(n)+2*tr(n-1)+tr(n-2)
