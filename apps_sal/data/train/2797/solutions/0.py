def mobile_keyboard(s):
    lookup = {c: i for s in '1,2abc,3def,4ghi,5jkl,6mno,7pqrs,8tuv,9wxyz,*,0,#'.split(',') for (i, c) in enumerate(s, start=1)}
    return sum((lookup[c] for c in s))
