is_polydivisible, get_polydivisible = (lambda digits: ((lambda ds: lambda s, b: (lambda f: (lambda x: x(x))(lambda y: f(lambda *xs: y(y)(*xs))))(lambda f: lambda l, n, xs: n % l == 0 and (not xs or f(l+1, n*b+xs.pop(), xs)))(1, ds[s[0]], [ds[i] for i in reversed(s[1:])]))({i:n for n,i in enumerate(digits)}), (lambda n, b: '0' if n == 1 else (lambda f: (lambda x: x(x))(lambda y: f(lambda *xs: y(y)(*xs))))(lambda f: lambda n, l, ds, xs: (xs[n][0] if n < len(xs) else f(n-len(xs), l+1, ds, [(s+d, x*b+i) for s,x in xs for i,d in enumerate(ds) if (x*b+i)%l==0])) if xs else None)(n - 2, 2, digits[:b], list(zip(digits, range(b)))[1:]))))('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
