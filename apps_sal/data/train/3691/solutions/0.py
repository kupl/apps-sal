def half(i, n):
    return "".join(str(d%10) for d in range(1, n-i+1))

def line(i, n):
    h = half(i, n)
    return " " * i + h + h[-2::-1]

def get_a_down_arrow_of(n):
    return "\n".join(line(i, n) for i in range(n))

