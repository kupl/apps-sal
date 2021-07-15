def hello(name = None):
    ans = ""
    if name is "" or name is None:
        return "Hello, World!"
    nm = list(name)
    for i in range(0, len(nm)):
        if i == 0:
            ans += nm[i].upper()
        else:
            ans += nm[i].lower()
    return "Hello, "+ans+"!"
        

