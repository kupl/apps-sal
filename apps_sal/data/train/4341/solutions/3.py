def solve(a,b):
    return ([a,b]           if not a or not b else
            solve(a%(2*b),b)  if a>=2*b else
            solve(a,b%(2*a))  if b>=2*a else
            [a,b])
