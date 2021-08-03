def say_hello(name, city, state):
    nstr = ""
    c = city
    s = state
    for n in name:
        nstr += n + " "
    nstr = nstr.strip()
    txt = 'Hello, {}! Welcome to {}, {}!'
    return txt.format(nstr, c, s)
