def decode(number):
    import textwrap
    arr = []
    for x in str(number).split('98'):
        if x:
            try:
                arr.append(str(int(x, 2)))
            except:
                arr.append("".join([chr(int(x) - 4) for x in textwrap.wrap(x, 3)]))
    return ", ".join(arr)
