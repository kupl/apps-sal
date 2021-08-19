def mobile_keyboard(s):
    a = '12abc3def4ghi5jkl6mno7pqrs8tuv9wxyz*0#'
    b = '11234123412341234123412345123412345111'
    d = {x: int(y) for (x, y) in zip(a, b)}
    return sum((d[x] for x in s))
