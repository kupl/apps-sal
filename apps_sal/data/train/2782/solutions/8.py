def calc(expr):
    print(expr)
    s = [0]
    for arg in expr.split(' '):
        try:
            s.append(float(arg))
        except:
            try:
                s.append(eval(f"{s.pop(-2)} {arg} {s.pop(-1)}"))
            except:
                pass

    return s[-1]
