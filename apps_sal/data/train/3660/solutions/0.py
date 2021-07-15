from math import factorial as f
count_paths=lambda n,c:f(c[0]+abs(n-c[1]-1))//(f(abs(n-c[1]-1))*f(c[0])) if n!=1 else 0
